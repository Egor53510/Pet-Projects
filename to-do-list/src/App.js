import React, { useState } from 'react';
import './App.css';
import ToDoList from './ToDoList';

function App() {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  const onAddTask = () => {
    if (task.trim()) {
      setTasks([...tasks, { text: task, completed: false }]);
      setTask('');
    }
  };

  const onChangeTask = (index) => {
    const newTasks = tasks.map((task, i) =>
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(newTasks);
  };

  const onDeleteTask = (index) => {
    const newTasks = tasks.filter((_, i) => i !== index);
    setTasks(newTasks);
  };

  const onSaveTasks = () => {
    const data = tasks.map(task => `${task.completed ? '[x]' : '[ ]'} ${task.text}`).join('\n');
    const blob = new Blob([data], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'tasks.txt';
    a.click();
    URL.revokeObjectURL(url);
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
        </div>
      </div>
      <ToDoList tasks={tasks} onChangeTask={onChangeTask} onDeleteTask={onDeleteTask} />
    </div>
  );
}

export default App;
