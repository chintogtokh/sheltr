import { Component } from 'react';
import { connect } from 'react-redux';
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