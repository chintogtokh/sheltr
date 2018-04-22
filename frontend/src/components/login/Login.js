import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import { connect } from 'react-redux';
// import { ToastContainer, toast } from 'react-toastify';
import './Login.css';
import { alertActions } from '../../actions';
import { userActions } from '../../actions';

class Login extends Component {

    componentDidMount = function() {
        document.title = "Sheltr | Login";
    }

    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: '',
            submitted: false
        };

        const { dispatch } = this.props;

        dispatch(alertActions.clear());

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

        this.onClick = this.onClick.bind(this);
    }

    handleChange(e) {
        const { name, value } = e.target;
        this.setState({ [name]: value });
    }

    handleSubmit(e) {
        e.preventDefault();

        this.setState({ submitted: true });
        const { username, password } = this.state;
        const { dispatch } = this.props;
        if (username && password) {
            dispatch(userActions.login(username, password));
        }
    }

    mustSubmitNotification = () => toast("Please contact our support staff to reset your password!",
      {
        type: toast.TYPE.INFO,
        autoClose: 5000,
        hideProgressBar: true,
        bodyClassName: "custom-toast"
      });

    onClick = function(e) {
        e.preventDefault();
        this.mustSubmitNotification();
    }


    render() {
        const { loggingIn } = this.props;
        const { username, password, submitted } = this.state;
        return (
            <div className="login-container">
            <ToastContainer />
                <h1>Login</h1>
                <div>
                  <form name="form" onSubmit={this.handleSubmit}>
                    <div className={'form-group' + (submitted && !username ? ' has-error' : '')}>
                      <label htmlFor="username">Username</label>
                      <input type="text" className="form-control" name="username" value={username} onChange={this.handleChange} />
                    </div>
                    <div className={'form-group' + (submitted && !password ? ' has-error' : '')}>
                        <label htmlFor="password">Password</label>
                      <input type="password" className="form-control" name="password" value={password} onChange={this.handleChange} />
                    </div>
                    <div className="form-group inline-button-group">
                      <button type="submit" className="btn btn-primary">Login</button>
                      {loggingIn &&
                          <span>&nbsp;<i className="fas fa-spinner fa-pulse"></i>&nbsp;</span>
                      }
                      <Link to="/auth/register" className="btn btn-light">Register</Link>
                      <button className="btn btn-link" onClick={this.onClick}>Forgot Password?</button>
                    </div>
                  </form>
                </div>
            </div>
        );
    }
}


function mapStateToProps(state) {
    const { loggingIn } = state.authentication;
    return {
        loggingIn
    };
}

export default connect(mapStateToProps)(Login);