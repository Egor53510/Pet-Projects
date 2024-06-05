import React from "react";
import ToDoItem from './ToDoItem';

function ToDoList({ tasks, onChangeTask, onDeleteTask }) {
    return (
        <ul>
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