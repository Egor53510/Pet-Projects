import React from "react";

class AddUser extends React.Component {
  userAdd = {}
    constructor(props) {
        super(props)
        this.state ={
            fname: "",
            lname: "",
            age: 1,
            isHappy: false
        }
    }
  render() {
    return (
      <form ref={(el) => this.myForm = el}>
        <input placeholder="Имя" onChange={(e) => this.setState({ fname: e.target.value })}/>
        <input placeholder="Фамилия" onChange={(e) => this.setState({ lname: e.target.value })}/>
        <input placeholder="Возраст" onChange={(e) => this.setState({ age: e.target.value })}/>
        <label htmlFor="isHappy">Счастлив?</label>
        <input type="checkbox" id="isHappy" onChange={(e) => this.setState({ isHappy: e.target.checked })}/>
        <button type="button" onClick={() => {
          this.myForm.reset()
          this.userAdd = {
              fname: this.state.fname,
              lname: this.state.lname,
              age: this.state.age,
              isHappy: this.state.isHappy
          }
          if(this.props.user)
            this.userAdd.id = this.props.user.id
          this.props.onAdd(this.userAdd)
        }
        }
      >Добавить</button>
      </form>
    )
  }
}


export default AddUser