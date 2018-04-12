import React from 'react';
import { Router, Route, Redirect, Switch } from 'react-router-dom';
import { connect } from 'react-redux';

import { history } from '../../helpers';
import { alertActions } from '../../actions';
import Login from '../login/Login';
import Logout from '../logout/Logout';
import Register from '../register/Register';
import PrivateRoute from '../PrivateRoute';
import './Auth.css'

class Auth extends React.Component {
    constructor(props) {
        super(props);

        const { dispatch } = this.props;
        history.listen((location, action) => {
            // clear alert on location change
            dispatch(alertActions.clear());
        });
    }

    render() {
        const { alert } = this.props;

        return (
            <div>
                <main role="main">
                <div className="auth-container">
                <div className="container">
                    <div className="container">
                        {alert.message &&
                            <div className={`alert ${alert.type}`}>{alert.message}</div>
                        }
                    </div>
                    <Switch>
                        <Route exact path="/auth/login" component={Login} />
                        <Route exact path="/auth/register" component={Register} />
                        <Route exact path="/auth/logout" component={Logout} />
                        <Route exact path="/auth" render={() => <Redirect to="/auth/login" />} />
                    </Switch>
                </div>
                </div>
                </main>
            </div>
        );
    }
}

function mapStateToProps(state) {
    const { alert } = state;
    return {
        alert
    };
}

export default connect(mapStateToProps)(Auth);