import React from "react";
import {IoCloseCircleSharp, IoHammerSharp } from 'react-icons/io5'

class User extends React.Component {
    user = this.props.user
  render() {
    return (
        <div className="user">
            <IoCloseCircleSharp className="delete"/>
            <IoHammerSharp className="edit"/>
            <h3>{ this.user.fname } { this.user.lname }</h3>
            <p>Age: { this.user.age }</p>
            </div>
    )
  }
}


export default User