import React from "react";

function ToDoItem({ task, onChange, onDelete }) {
    return(
        <li>
            <span
                style={{
                    textDecoration: task.completed ? 'line-through': 'none'
                }}
                onClick={onChange}
            >
                {task.text}
            </span>
            <button onClick={onDelete}>Delete</button>
        </li>
    )
}

export default ToDoItem;