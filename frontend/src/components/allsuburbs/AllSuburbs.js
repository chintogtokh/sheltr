import React, { Component } from 'react';
import './AllSuburbs.css';
import { connect } from 'react-redux';
import { browseActions } from '../../actions';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';

class AllSuburbs extends Component {

  constructor(props) {
    super(props);
    const { dispatch } = this.props;
    this.state = {
    };
  }

  componentDidMount() {
    let { preferences} = this.props;
    fetch('/api/suburbs/')
        .then(response => response.json().then( data => ({
            data: data,
            status: response.status
            })
        ))
        .then(response => {
            if (response.status !== 200) {
                // dispatch({
                //     type: suburbConstants.SUBURB_NOTFOUND,
                // })
                console.log("error.");
            }
            else{
              this.setState({suburbs: response.data});
            }
        });

  }

  render() {
    let { preferences} = this.props;
    let { suburbs } = this.state;
    preferences = JSON.stringify(preferences);
    suburbs = JSON.stringify(suburbs);
      return (
      <div>
          <main role="main">
            <div className="container">

                    <h1>...here are the top 5 suburbs</h1>

                    {preferences}

                    <hr/>

                    {suburbs}


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