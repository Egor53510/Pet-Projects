import React from "react";
import ToDoItem from './ToDoItem';

function ToDoList({ tasks, onChangeTask, onDeleteTask }) {
    return (
        <ul className="task-list">
            {tasks.map((task, index) => (
                <ToDoItem
                    key={index}
                    task={task}
                    onChange={() => onChangeTask(index)}
                    onDelete={() => onDeleteTask(index)}
                />
            ))}
        </ul>
    )
}

export default ToDoList;