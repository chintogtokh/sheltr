import React, { Component } from 'react';
import './AllSuburbs.css';
import { connect } from 'react-redux';
import { suburbActions } from '../../actions';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';

class AllSuburbs extends Component {

  constructor(props) {
        super(props);
        const { dispatch } = this.props;
    }

  render() {
    const { suburb, extract, coords} = this.props;
      return (
      <div>
          <main role="main">
            <div className="container">

                    <h1>...here are the top 5 suburbs</h1>


                </div>
          </main>
      </div>
      );
  }
}

const mapStateToProps = state => ({
  preferences: state.browse
});

export default connect(mapStateToProps)(AllSuburbs);