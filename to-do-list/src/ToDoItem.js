import React from "react";

function ToDoItem({ task, onChange, onDelete }) {
    return(
        <li className={task.completed ? "checked" : ""}>
            <span
                style={{
                    textDecoration: task.completed ? 'line-through' : 'none'
                }}
                onClick={onChange}
            >
                {task.text}
            </span>
            <button className="close" onClick={onDelete}>X</button>
        </li>
    )
}

export default ToDoItem;