import React, { Component } from 'react';

class Footer extends Component {

  state = {
    users:[]
  }

  render() {
    return (
      <div>
        <footer class="container">
          <p class="float-right"><a href="#">back to top</a></p>
          <p>built with <i class="fas fa-heart"></i> in Melbourne by team saladandscrambedeggs &middot; <a href="#">about</a> &middot; <a href="#">contact</a></p>
        </footer>
      </div>
    );
  }
}

export default Footer;
