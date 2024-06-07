import React, { useState, useEffect } from 'react';
import './App.css';
import ToDoList from './ToDoList';

function App() {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const savedTasks = JSON.parse(localStorage.getItem('tasks'));
    if (savedTasks){
      setTasks(savedTasks);
    }
  }, []);

  const onAddTask = () => {
    if (task.trim()) {
      const newTasks = [...tasks, { text: task, completed: false }];
      setTasks(newTasks);
      localStorage.setItem('tasks', JSON.stringify(newTasks));
      setTask('');
    }
  };

  const onChangeTask = (index) => {
    const newTasks = tasks.map((task, i) =>
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(newTasks);
    localStorage.setItem('tasks', JSON.stringify(newTasks));
  };

  const onDeleteTask = (index) => {
    const newTasks = tasks.filter((_, i) => i !== index);
    setTasks(newTasks);
    localStorage.setItem('tasks', JSON.stringify(newTasks));
  };


  return (
    <div>
      <div className="header">
        <h1>ToDo List</h1>
        <div className="input-container">
          <input
            type="text"
            placeholder="Type your task"
            value={task}
            onChange={(e) => setTask(e.target.value)}
          />
          <button className="addBtn" onClick={onAddTask}>
            Add Item
          </button>
          <button className="addBtn" onClick={() => localStorage.setItem('tasks', JSON.stringify(tasks))}>
          Save Tasks
        </button>
        </div>
      </div>
      <ToDoList tasks={tasks} onChangeTask={onChangeTask} onDeleteTask={onDeleteTask} />
    </div>
  );
}

export default App;
