import React from "react";
import Header from "./components/Header";
import Users from "./components/Users";
import AddUser from "./components/AddUser";

class App extends React.Component{
  constructor(props){
    super(props)
        this.state={
            users: [
            {
                id: 1,
                fname: 'Egor',
                lname: 'Dudov',
                age: 20,
                isHappy: true
            },
            {
                id: 2,
                fname: 'Polina',
                lname: 'Dudova',
                age: 18,
                isHappy: false
            }
        ]
    }
    this.addUser = this.addUser.bind(this)
}
  render() { 
    return (
      <div className="name">
        <Header text="Список пользователей" />
        <main>
          <Users users={this.state.users}/>
        </main>
        <aside>
          <AddUser onAdd={this.addUser}/>
        </aside>
      </div>
      )
  }

  addUser(user) {
    console.log(user)
    const id = this.state.users.length + 1
    this.setState({ users: [...this.state.users, {id, ...user}] })
  }
}

export default App