import pandas as pd
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/Spotify Million Song Dataset_exported.csv")

# Normalize columns
df.columns = df.columns.str.lower().str.strip()

# Rename
df = df.rename(columns={
    "text": "lyrics",
    "song": "title"
})

df = df.dropna(subset=["lyrics", "title", "artist"])

# Clean lyrics
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

df["lyrics"] = df["lyrics"].apply(clean_text)

# Reduce size for demo
df = df.sample(15000, random_state=42)

# TF-IDF
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=15000
)
tfidf_matrix = vectorizer.fit_transform(df["lyrics"])

# Prediction function
def find_song(snippet, top_k=3):
    snippet = clean_text(snippet)
    snippet_vec = vectorizer.transform([snippet])

    similarities = cosine_similarity(snippet_vec, tfidf_matrix)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = df.iloc[top_indices][["title", "artist"]]
    return results

# Example
print(find_song("we were both young when I first saw you"))
