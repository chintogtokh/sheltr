import React, { Component } from 'react';
import { HashLink } from 'react-router-hash-link';

import './Footer.css';

class Footer extends Component {

  state = {
    users:[]
  }

  render() {
    return (
      <div>
        <footer className="container">
          <p>
          made with <i className="fas fa-heart"></i> in Melbourne by team saladandscrambedeggs &middot; &nbsp;
          <HashLink smooth to="/#about" scroll={el => el.scrollIntoView({ behavior: "smooth", block: 'start' })}>about</HashLink>
          &nbsp;&middot;&nbsp;
          <HashLink to="/contact">contact</HashLink>&nbsp;&middot;&nbsp;
          <HashLink to="/credits">credits</HashLink>
          </p>
        </footer>
      </div>
    );
  }
}

export default Footer;
