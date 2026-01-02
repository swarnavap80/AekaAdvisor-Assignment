const express = require("express");
const dotenv = require("dotenv");
dotenv.config();
const connectDB = require("./config/db.cjs");


connectDB();

const app = express();
app.use(express.json());

app.use("/api/auth", require("./routes/authRoutes.cjs"));
app.use("/api", require("./routes/taskRoutes.cjs"));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on ${PORT}`));
