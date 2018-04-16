import React, { Component } from 'react';
import './Suburb.css';
import { connect } from 'react-redux';
import { suburbActions } from '../../actions';

class Suburb extends Component {

  constructor(props) {
        super(props);

        const suburbName = props.match.params.name;

        const { dispatch } = this.props;
        dispatch(suburbActions.fetchSuburb(suburbName));

    }

  render() {
    const { suburb } = this.props;
      return (
      <div>
          <main role="main">
            { suburb &&
              <div className="container">
                  <h1>{suburb.name}</h1>
              </div>
            }
            { !suburb &&
              <div className="container">
                  <h1>Suburb not found :(</h1>
                  <pre>Try another one?</pre>
              </div>
            }
          </main>
      </div>
      );
  }
}

const mapStateToProps = state => ({
  suburb: state.suburb.suburb,
});

// export default connect(mapStateToProps)(Suburb);

export default connect(mapStateToProps)(Suburb);