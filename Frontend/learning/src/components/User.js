import React from "react";
import AddUser from "./AddUser";
import {IoCloseCircleSharp, IoHammerSharp } from 'react-icons/io5'

class User extends React.Component {
  constructor(props){
    super(props)
        this.state={
          editForm: false
        }
      }
    user = this.props.user
  render() {
    return (
        <div className="user">
            <IoCloseCircleSharp onClick={() => this.props.onDelete(this.user.id)} className="delete"/>
            <IoHammerSharp onClick={() => {
              this.setState({
                editForm: !this.state.editForm
              })
            }} className="edit" />
            <h3>{ this.user.fname } { this.user.lname }</h3>
            <p>Age: { this.user.age }</p>

            {this.state.editForm && <AddUser user={this.user} onAdd={this.props.onEdit} />}
            </div>
    )
  }
}


export default User