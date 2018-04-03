import React, { Component } from 'react';
import './Navbar.css';
import full_logo from '../../files/full_logo.svg';

class Navbar extends Component {

  state = {
    active:""
  }

  render() {
    return (
      <nav className="navbar navbar-expand-md navbar-dark fixed-top">
          <a className="navbar-brand" href="/">
              <img src={full_logo} alt="Sheltr logo"/>
          </a>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarCollapse">
          </div>
      </nav>
    );
  }
}

export default Navbar;