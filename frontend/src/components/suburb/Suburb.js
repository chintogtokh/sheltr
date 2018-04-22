import React, { Component } from 'react';
import './Suburb.css';
import { connect } from 'react-redux';
import { suburbActions } from '../../actions';
import { Map, TileLayer, GeoJSON } from 'react-leaflet';
import bbox from 'turf-bbox';
import Select from 'react-select';


class Suburb extends Component {

  constructor(props) {
      super(props);

      this.state = {
        'suburb': null
      }

      const suburbName = props.match.params.name;

      this.handleSelectChange = this.handleSelectChange.bind(this);



  }

  componentWillMount() {

    let suburb_shim = this.props.match.params.name;

    fetch('/api/suburbs/' + suburb_shim)
        .then(response => response.json().then( data => ({
            data: data,
            status: response.status
            })
        ))
        .then(response => {
            if (response.status !== 200) {
                return;
            }
            else{
              let bboxArray;// = bbox(suburb.geojson);
              let corner1;// = [bboxArray[1], bboxArray[0]];
              let corner2;// = [bboxArray[3], bboxArray[2]];
              let bounds;// = [corner1, corner2];

              // let suburb = this.state.suburb;

              bboxArray = bbox(response.data.geojson);
              corner1 = [bboxArray[1], bboxArray[0]];
              corner2 = [bboxArray[3], bboxArray[2]];
              bounds = [corner1, corner2];

                this.setState({suburb: response.data, bounds: bounds});

                document.title = "Sheltr | " + this.state.suburb.name;

                const { dispatch } = this.props;
                dispatch(suburbActions.fetchSuburbWiki(this.state.suburb.name));
            }
        });
  }

  getStyle(feature, layer) {
    return {
      color: '#112660',
      weight: 5,
      opacity: 0.65
    }
  };

  getSuburbs (input) {
    if (!input) {
          return Promise.resolve({ options: [] });
    }

    return fetch(`/api/search/suburbs?q=${input}`)
    .then((response) => response.json())
    .then((json) => {
      return { options:json };
    });
  }

  handleSelectChange = function(value) {
    window.open('/suburb/' + value.shim);
  };

  numberToRanking = (num) => {
    let tmp = { '0': 'irrelevant',
                      '10':  'very important',
                      '7':  'moderately important',
                      '4':  'important',
                      '1':  'not important'}
    return tmp[num.toString()];
  }

  render() {
      const { wiki, selected_suburb, preferences} = this.props;

      return (
      <div>
          <main role="main">
            { this.state.suburb &&
              <div className="container">
                  <h1>{this.state.suburb.name}</h1>

                  <div className="row">
                    <div className="col-md-8">
                    <p>
                    {wiki}
                    </p>

                    <h3>main indicators</h3>
                    <ul>
                      <li>Affordability rating - {this.state.suburb.rating_affordability} { preferences.affordability && <span>- your preference was <b>{this.numberToRanking(preferences.affordability)}</b></span>}</li>
                      <li>Safety rating - {this.state.suburb.rating_safety} { preferences.crimeSafety &&  <span>- your preference was <b>{this.numberToRanking(preferences.crimeSafety)}</b></span>}</li>
                      {preferences.raw_uni && <li>University rating - {this.state.suburb.universities[preferences.raw_uni.shim]} - your university was <b>{preferences.raw_uni.name}</b></li>}
                      {preferences.language && preferences.language!=0 && <li>Language rating - {this.state.suburb.language[preferences.raw_actualLanguage.shim]} - your preference was <b>{this.numberToRanking(preferences.language)}</b> and your language was <b>{preferences.raw_actualLanguage.name}</b></li>}
                    </ul>

                    <h3>stats</h3>
                    <ul>
                    {
                      this.state.suburb.stats.map((value, index) => {
                        return <li key={index}>{value.desc} - {value.number}</li>
                       })
                    }
                    </ul>


                    <h3>rentals here</h3>
                    <ul>
                      <li><a href={"https://www.domain.com.au/rent/?terms=" + this.state.suburb.name.toLowerCase() + " vic"}>Domain.com.au</a></li>
                    <li><a href={"https://www.realestate.com.au/rent/in-" + this.state.suburb.name.toLowerCase() + ",+vic/list-1"}>Realestate.com.au</a></li>
                    </ul>

                    <h3>or...</h3>
                    <Select.Async
                  placeholder = "search for another suburb?"
                  name="selected_suburb"
                  autoload = {true}
                  className = "react-select-single-suburb"
                  value={selected_suburb}
                  valueKey="shim"
                  labelKey="name"
                  onChange={this.handleSelectChange}
                  loadOptions={this.getSuburbs}
                  backspaceRemoves={true} />

                    {/*
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
                      </div> */}
                    </div>
                    <div className="col-md-4">

                  <br/>

                    {this.state.suburb &&
                      <Map style={{'height':500+'px','width':100+'%'}} bounds={this.state.bounds}>
                            <TileLayer
                              attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <GeoJSON key={this.state.suburb.shim} data={this.state.suburb.geojson} style={this.getStyle} />
                        </Map>
                      }
                    </div>
                  </div>

              </div>
            }
            { !this.state.suburb &&
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
  preferences: state.browse,
  wiki: state.suburb.wiki_extract
});

// export default connect(mapStateToProps)(Suburb);

export default connect(mapStateToProps)(Suburb);