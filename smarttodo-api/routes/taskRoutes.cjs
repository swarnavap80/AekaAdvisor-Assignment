const express = require("express");
const router = express.Router();
const auth = require("../middleware/authMiddleware.cjs");
const task = require("../controller/taskController.cjs");

router.post("/tasks", auth, task.createTask);
router.get("/tasks", auth, task.getTasks);
router.put("/tasks/:id", auth, task.updateTask);
router.delete("/tasks/:id", auth, task.deleteTask);

module.exports = router;
