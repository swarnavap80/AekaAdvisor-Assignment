const User = require("../models/User.cjs");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

exports.register = async (req, res) => {
  try {
    console.log(req.body); // DEBUG LINE

    const { email, password } = req.body || {};

    if (!email || !password) {
      return res.status(400).json({
        message: "Email and password are required"
      });
    }

    
    res.json({ message: "Register works" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Server error" });
  }
};


exports.login = async (req, res) => {
  try {
    console.log("LOGIN BODY:", req.body); // debug

    const { email, password } = req.body || {};

    if (!email || !password) {
      return res.status(400).json({
        message: "Email and password are required"
        
      });
      

    }
     const token = jwt.sign(
      { user: { id: User._id } },
      process.env.JWT_SECRET,
      { expiresIn: "2h" }
    );  

    // 5. SEND TOKEN ✅
    res.json({ token });

    // continue login logic here
    res.json({ message: "Login route working" });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Server error" });
  }
};

