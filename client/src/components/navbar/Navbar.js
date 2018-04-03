import React, { Component } from 'react';
import './Navbar.css';
import { Link } from "react-router-dom";
import full_logo from '../../files/full_logo.svg';

class Navbar extends Component {

  state = {
    active:""
  }

  render() {
    return (
      <nav className="navbar navbar-expand-md navbar-dark fixed-top">
        <Link to="/" className="navbar-brand"><img src={full_logo} alt="Sheltr logo"/></Link>
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