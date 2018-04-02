import React, { Component } from 'react';
import logo from './logo.svg';
import './Home.css';

console.log("D");

class Home extends Component {

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
      <div className="Home">
        <header className="Home-header">
          <img src={logo} className="Home-logo" alt="logo" />
          <h1 className="Home-title">Welcome to Sheltr</h1>
        </header>
        <p className="Home-intro">
          <h1>All users</h1>
          {this.state.users.map(user => <div key={user.id}>{user.username}</div>
            )}
        </p>
      </div>
    );
  }
}

export default Home;
