import React, { Component } from 'react';
import './Login.css';

class Login extends Component {

    render() {
        return (
        <div>
          <main role="main">
            <div className="login-container">
              <div className="container">
                <h1>Login</h1>
                <div>
                  <form name="form">
                    <div className="form-group">
                      <label for="username">Username</label>
                      <input type="text" className="form-control" name="username" value="" />
                    </div>
                    <div className="form-group"><label for="password">Password</label>
                      <input type="password" className="form-control" name="password" value="" />
                    </div>
                    <div className="form-group inline-button-group">
                      <button type="button" className="btn btn-primary">Login</button>
                      <button type="button" className="btn btn-light">Register</button>
                      <button type="button" className="btn btn-light"><i className="fab fa-google"></i> Login with Google</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </main>
        </div>
        );
    }
}

export default Login;
