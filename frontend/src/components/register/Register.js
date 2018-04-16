import React from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { userActions } from '../../actions';
import './Register.css';
import { history } from '../../helpers';
import { alertActions } from '../../actions';

class Register extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            user: {
                first_name: '',
                last_name: '',
                username: '',
                password: ''
            },
            submitted: false
        };

        const { dispatch } = this.props;
        dispatch(alertActions.clear());

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        const { name, value } = event.target;
        const { user } = this.state;
        this.setState({
            user: {
                ...user,
                [name]: value
            }
        });
    }

    handleSubmit(event) {
        event.preventDefault();

        this.setState({ submitted: true });
        const { user } = this.state;
        const { dispatch } = this.props;
        if (user.first_name && user.last_name && user.username && user.password) {
            dispatch(userActions.register(user));
        }
    }

    render() {
        const { registering  } = this.props;
        const { user, submitted } = this.state;
        return (

            <div className="register-container">
              <div className="container">
                <h1>Register</h1>
                <div>
                    <form name="form" onSubmit={this.handleSubmit}>
                        <div className={'form-group' + (submitted && !user.first_name ? ' has-error' : '')}>
                            <label htmlFor="first_name">First Name</label>
                            <input type="text" className="form-control" name="first_name" value={user.first_name} onChange={this.handleChange} />
                            {submitted && !user.first_name &&
                                <div className="help-block">First Name is required</div>
                            }
                        </div>
                        <div className={'form-group' + (submitted && !user.last_name ? ' has-error' : '')}>
                            <label htmlFor="last_name">Last Name</label>
                            <input type="text" className="form-control" name="last_name" value={user.last_name} onChange={this.handleChange} />
                            {submitted && !user.last_name &&
                                <div className="help-block">Last Name is required</div>
                            }
                        </div>
                        <div className={'form-group' + (submitted && !user.username ? ' has-error' : '')}>
                            <label htmlFor="username">Username</label>
                            <input type="text" className="form-control" name="username" value={user.username} onChange={this.handleChange} />
                            {submitted && !user.username &&
                                <div className="help-block">Username is required</div>
                            }
                        </div>
                        <div className={'form-group' + (submitted && !user.password ? ' has-error' : '')}>
                            <label htmlFor="password">Password</label>
                            <input type="password" className="form-control" name="password" value={user.password} onChange={this.handleChange} />
                            {submitted && !user.password &&
                                <div className="help-block">Password is required</div>
                            }
                        </div>
                        <div className="form-group">
                            <button className="btn btn-primary">Register</button>
                            {registering &&
                                <span>&nbsp;<i className="fas fa-spinner fa-pulse"></i>&nbsp;</span>
                            }
                            <Link to="/auth/login" className="btn btn-link">Cancel</Link>
                        </div>
                    </form>
                </div>
              </div>
            </div>
        );
    }
}

function mapStateToProps(state) {
    const { registering } = state.registration;
    return {
        registering
    };
}


export default connect(mapStateToProps)(Register);