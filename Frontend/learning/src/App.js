import React from "react";
import Header from "./components/Header";

class App extends React.Component{
  render() { 
    return (
      <div className="name">
        <Header text="Шапка сайта" />
        <input placeholder="help text" 
        onClick={this.inputClick}/>
      </div>
      )
  }

  inputClick() { console.log("clicked") }
}

export default App