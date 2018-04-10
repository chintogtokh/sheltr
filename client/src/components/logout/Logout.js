import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { ToastContainer, toast } from 'react-toastify';
import { userActions } from '../../actions';

class Logout extends Component {

    componentWillMount () {
        this.props.dispatch(userActions.logout());
        this.props.history.push('/');
    }

    render() {
        return null;
    }
}

export default connect()(Logout);