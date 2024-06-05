//import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import ToDoList from './ToDoList';

function App() {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  const onAddTask = () => {
    if (task.trim()) {
      setTasks([...tasks, {text: task, completed: false}]);
      setTask('');
    }
  };

  const onChangeTask = (index) => {
    const newTasks = tasks.map((task, i) => 
    i === index ? {...task, completed: !task.completed} : task
  )
  setTasks(newTasks);
  }

  const onDeletetask = (index) => {
    const newTasks = tasks.filter((_, i) => i !== index);
    setTasks(newTasks);
  }

  return (
    <div className="App">
      <h1>ToDo List</h1>
      <input 
        type='text'
        placeholder='Type your task' 
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button onClick={onAddTask}>Add Item</button>
      <ToDoList tasks={tasks} onChangeTask={onChangeTask} onDeleteTask={onDeletetask} />
    </div>
  );
}

export default App;
