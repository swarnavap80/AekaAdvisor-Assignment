const Task = require("../models/Task.cjs");
const mongoose = require('mongoose');

exports.createTask = async (req, res) => {

  console.log(req.body);
  
  const task = await Task.create({
    user: req.user.id,
    title: req.body.title,
    description: req.body.description
  });
  res.json(task);
};

exports.getTasks = async (req, res) => {
  const tasks = await Task.find({ user: req.user.id });
  res.json(tasks);
};

exports.updateTask = async (req, res) => {
  const task = await Task.findById(req.params.id);
  if (!task) return res.status(404).json({ message: "Task not found" });

 if (!task.user || !req.user || !req.user.id) {
  return res.status(401).json({ message: "Unauthorized" });
}

if (task.user.toString() !== req.user.id.toString()) {
  return res.status(401).json({ message: "Unauthorized" });
}

  Object.assign(task, req.body);
  await task.save();
  res.json(task);
};

exports.deleteTask = async (req, res) => {
  await Task.findByIdAndDelete(req.params.id);
  res.json({ message: "Task deleted" });
};
