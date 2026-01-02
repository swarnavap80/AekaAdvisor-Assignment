import pandas as pd

def recommend_places(source_city, top_n=5):
    # Load dataset
    df = pd.read_csv("data/Top Indian Places to Visit.csv")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Rename important columns for clarity
    df = df.rename(columns={
        "name": "place",
        "google review rating": "rating",
        "number of google review in lakhs": "popularity"
    })

    # Check source city
    source = df[df["city"].str.lower() == source_city.lower()]
    if source.empty:
        raise ValueError("Source city not found in dataset")

    source_city = source.iloc[0]["city"]
    source_state = source.iloc[0]["state"]
    source_zone = source.iloc[0]["zone"]

    # Remove same city
    df = df[df["city"].str.lower() != source_city.lower()]

    # Proximity score
    def proximity(row):
        if row["state"] == source_state:
            return 1.0
        elif row["zone"] == source_zone:
            return 0.6
        else:
            return 0.3

    df["proximity_score"] = df.apply(proximity, axis=1)

    # Normalize rating & popularity
    df["rating_norm"] = df["rating"] / df["rating"].max()
    df["popularity_norm"] = df["popularity"] / df["popularity"].max()

    # Final score
    df["score"] = (
        0.45 * df["rating_norm"] +
        0.35 * df["popularity_norm"] +
        0.20 * df["proximity_score"]
    )

    return df.sort_values("score", ascending=False).head(top_n)[
        ["place", "city", "state", "zone", "rating", "popularity", "score"]
    ]

if __name__ == "__main__":
    print("\nTop weekend destinations from Kolkata:\n")
    print(recommend_places("Kolkata"))

    print("\nTop weekend destinations from Delhi:\n")
    print(recommend_places("Delhi"))

    print("\nTop weekend destinations from Bangalore:\n")
    print(recommend_places("Bangalore"))
