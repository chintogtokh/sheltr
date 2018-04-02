import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

  state = {
    users:[]
  }

  componentDidMount() {
    fetch('/users')
    .then(res => res.json())
    .then(users => this.setState({users}));
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Sheltr</h1>
        </header>
        <p className="App-intro">
          <h1>All users</h1>
          {this.state.users.map(user => <div key={user.id}>{user.username}</div>
            )}
        </p>
      </div>
    );
  }
}

export default App;
