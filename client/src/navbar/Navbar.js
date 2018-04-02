import React, { Component } from 'react';
import logo from '../files/logo.svg';

class Navbar extends Component {

  state = {
    active:""
  }

  render() {
    return (
      <nav class="navbar navbar-expand-md navbar-dark fixed-top">
          <a class="navbar-brand" href="#">
              <img src="images/sheltr_logo.png" />
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
          </div>
      </nav>
    );
  }
}

export default Navbar;