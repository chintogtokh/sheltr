import React, { Component } from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import full_logo from '../../files/full_logo.svg';

class Navbar extends Component {

  render() {
    const { user, loggedIn } = this.props;
    return (
      <nav className="navbar navbar-expand-md navbar-dark fixed-top">
        <Link to="/" className="navbar-brand"><img src={full_logo} alt="Sheltr logo"/></Link>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarCollapse">
          {!loggedIn &&
            <ul className="navbar-nav flex-row ml-md-auto d-none d-md-flex">
                <li className="nav-item">
                  <Link to="/auth/login" className="nav-link">Login</Link>
                </li>
                <li className="nav-item">
                  <Link to="/auth/register" className="nav-link">Register</Link>
                </li>
            </ul>
          }
          {loggedIn &&
            <ul className="navbar-nav flex-row ml-md-auto d-none d-md-flex">
                <li className="nav-item">
                  <Link to="/auth/logout" className="nav-link">Logout ({user.username})</Link>
                </li>
            </ul>
          }
        </div>
      </nav>
    );
  }
}

function mapStateToProps(state) {
    const { loggedIn, user } = state.authentication;
    return {
        loggedIn, user
    };
}

export default connect(mapStateToProps)(Navbar);
