import React, { Component } from 'react';
import './Suburb.css';
import { connect } from 'react-redux';
import { suburbActions } from '../../actions';
import { Map, TileLayer, GeoJSON } from 'react-leaflet';
import bbox from 'turf-bbox';

class Suburb extends Component {

  constructor(props) {
        super(props);

        const suburbName = props.match.params.name;

        const { dispatch } = this.props;
        dispatch(suburbActions.fetchSuburb(suburbName));
        // dispatch(suburbActions.fetchSuburbWiki(suburbName));

    }

    getStyle(feature, layer) {
    return {
      color: '#006400',
      weight: 5,
      opacity: 0.65
    }
  };

  componentDidMount(){

  }

  render() {
    const { suburb, extract} = this.props;
    const bboxArray = bbox(suburb.geojson);
    const corner1 = [bboxArray[1], bboxArray[0]];
    const corner2 = [bboxArray[3], bboxArray[2]];
    const bounds = [corner1, corner2];

      return (
      <div>
          <main role="main">
            { suburb &&
              <div className="container">
                  <h1>{suburb.name}</h1>
                  <br/>
                  <div className="row">
                    <div className="col-md-8">
                    <p>
                    {extract}
                    </p>
                      <div className="media">
                        <img className="mr-3" src="/images/suburb_icons/teamwork.png" alt="Population" />
                        <div className="media-body">
                          <h5 className="mt-0">Population</h5>
                          {suburb.population}
                        </div>
                      </div>

                      <div className="media">
                        <img className="mr-3" src="/images/suburb_icons/savings.png" alt="Population" />
                        <div className="media-body">
                          <h5 className="mt-0">Rent</h5>
                          {suburb.average_rental}
                        </div>
                      </div>
                    </div>
                    <div className="col-md-4">

                      <Map style={{'height':500+'px','width':100+'%'}} bounds={bounds}>
                            <TileLayer
                              attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <GeoJSON key={suburb.shim} data={suburb.geojson} style={this.getStyle} />
                        </Map>

                    </div>
                  </div>

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
  extract: state.suburb.wiki_extract
});

// export default connect(mapStateToProps)(Suburb);

export default connect(mapStateToProps)(Suburb);