import React, { Component } from 'react';
import './Suburb.css';
import { connect } from 'react-redux';
import { suburbActions } from '../../actions';
import { Map, TileLayer, GeoJSON, Marker, Popup } from 'react-leaflet';
import bbox from 'turf-bbox';
import Select from 'react-select';
import ReactDOM from 'react-dom';
import ReactStreetview from 'react-streetview';
// import detective from '../../files/detective.svg';
// import chat from '../../files/chat.svg';
// import credit_card from '../../files/credit_card.svg';
// import university from '../../files/university.svg';

class Suburb extends Component {

  constructor(props) {
      super(props);

      this.state = {
        'suburb': null
      }

      this.handleSelectChange = this.handleSelectChange.bind(this);

  }

  getStatFromArray(arr, desc) {
    return arr[desc];
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

                this.setState({streetViewPanoramaOptions: {
                  addressControl: false,
                  disableDefaultUI: true,
                  showRoadLabels: false,
                    position: {lat: response.data.coords.lat, lng: response.data.coords.lng},
                    pov: {heading: 100, pitch: 0},
                    zoom: 1
                }});


                // if(this.state.uni_coords){
                //   var newbounds = bounds;
                //   console.log(newbounds);

                //   if(this.state.uni_coords.lat>this.state.bounds[0][0]){
                //     //newbounds[0][0] = this.state.uni_coords.lat;
                //   }
                //   if(this.state.uni_coords.lng>this.state.bounds[0][1]){
                //     newbounds[0][1] = this.state.uni_coords.lng;
                //   }

                //   if(this.state.uni_coords.lat<this.state.bounds[1][0]){
                //     newbounds[1][0] = this.state.uni_coords.lat;
                //   }
                //   if(this.state.uni_coords.lng<this.state.bounds[1][1]){
                //     //newbounds[1][1] = this.state.uni_coords.lng;
                //   }

                //   console.log(newbounds);
                //   this.setState({bounds: newbounds});
                //   this.setState({boundsUpdated: true});
                // }

            }
        });

    fetch('/api/university/' + this.props.preferences.raw_uni.shim)
        .then(response => response.json().then( data => ({
            data: data,
            status: response.status
            })
        ))
        .then(response => {
            this.setState({uni_coords: response.data.coords});

            // if(this.state.bounds){
            //       var newbounds = this.state.bounds;
            //       console.log(newbounds);

            //       if(response.data.coords.lat>this.state.bounds[0][0]){
            //         //newbounds[0][0] = response.data.coords.lat;
            //       }
            //       if(response.data.coords.lng>this.state.bounds[0][1]){
            //         newbounds[0][1] = response.data.coords.lng;
            //       }

            //       if(response.data.coords.lat<this.state.bounds[1][0]){
            //         newbounds[1][0] = response.data.coords.lat;
            //       }
            //       if(response.data.coords.lng<this.state.bounds[1][1]){
            //         //newbounds[1][1] = response.data.coords.lng;
            //       }

            //       console.log(newbounds);
            //       this.setState({bounds: newbounds});
            //       this.setState({boundsUpdated: true});
            //     }

            //this.setState({suburb: response.data, bounds: bounds});

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
    let tmp = {     '10':  'high priority',
                      '7':  'moderate priority',
                      '4':  'neutral',
                      '1':  'low priority',
                      '0':  'not a priority'}
    return tmp[num.toString()];
  };

  numberToColor = (num) => {
    num = parseInt(num,10);
    if(num>70){
      return "badge-success";
    }
    else if(num>40){
      return "badge-warning";
    }
    else{
      return "badge-danger";
    }
  }

  numberToWords = (name,num) => {
    num = parseInt(num,10);
    if(num>80){
      switch(name){
        case "safety": return "very safe";
        case "affordability": return "very affordable";
        case "language":  return "many students";
        case "uni": return "very close";
        default: return "";
      }
    }
    else if(num>60){
      switch(name){
        case "safety": return "safe";
        case "affordability": return "affordable";
        case "language":  return "some students";
        case "uni": return "close";
        default: return "";
      }
    }
    else if (num>40){
      switch(name){
        case "safety": return "kinda safe";
        case "affordability": return "kinda affordable";
        case "language":  return "few students";
        case "uni": return "far";
        default: return "";
      }
    }
    else{
      switch(name){
        case "safety": return "unsafe";
        case "affordability": return "unaffordable";
        case "language":  return "no students";
        case "uni": return "very far";
        default: return "";
      }
    }
  }


  render() {
      const { wiki, selected_suburb, preferences} = this.props;

      const googleMapsApiKey = 'AIzaSyAtl3mboWdO7jxiQHdSHqg97WHHig53LaQ';

      // see https://developers.google.com/maps/documentation/javascript/3.exp/reference#StreetViewPanoramaOptions



      return (
      <div id="SuburbComponent">



          <main role="main">

            { this.state.suburb &&

              <div>

              {
                this.state.streetViewPanoramaOptions &&
                <div>
                <div className="streetview-container">
                    <div style={{
                      width: '100%',
                      height: '100%',
                      backgroundColor: 'white'
                  }}>
                      <ReactStreetview
                          apiKey={googleMapsApiKey}
                          streetViewPanoramaOptions={this.state.streetViewPanoramaOptions}
                      />
                  </div>
                </div>
                <div className="streetview-container-after">
                </div>
                </div>
              }

              <div className="container">

              <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item"><a href="/">Home</a></li>
                  <li class="breadcrumb-item"><a href="/suburb">Suburb Suggestions</a></li>
                  <li class="breadcrumb-item active" aria-current="page">{this.state.suburb.name}</li>
                </ol>
              </nav>



                <div className="row">
                  <div className="col-md-8">
                    <h1>{this.state.suburb.name}</h1>
                  </div>

                  <div className="col-md-4">
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
                  </div>
                </div>



                  <div className="row">
                    <div className="col-md-8">
                    <p>
                    {wiki} {wiki && <a className="wiki-link" href={"https://en.wikipedia.org/wiki/" + this.state.suburb.name + ", Victoria"}><i>(data automatically extracted from Wikipedia)</i></a>}
                    </p>

                    <h3>
                    Main indicators
                    </h3>
                    <ul className="rating-list">

                      <li> Safety rating <span className={"badge badge-pill " + this.numberToColor(this.state.suburb.rating_safety)}>{this.numberToWords("safety",this.state.suburb.rating_safety)}</span> { preferences.crimeSafety &&  <span> your preference was {this.numberToRanking(preferences.crimeSafety)}</span>}{ !preferences.crimeSafety && <span> you did not input a preference</span>}</li>

                      <li> Affordability rating <span className={"badge badge-pill " + this.numberToColor(this.state.suburb.rating_affordability)}>{this.numberToWords("affordability",this.state.suburb.rating_affordability)}</span> { preferences.affordability && <span> your preference was {this.numberToRanking(preferences.affordability)}</span>}{ !preferences.affordability && <span> you did not input a preference</span>}</li>


                      {preferences.language && preferences.language!==0 &&

                        <li>
                          International student language rating for {preferences.raw_actualLanguage.name} <span className={"badge badge-pill " + this.numberToColor(this.state.suburb.language[preferences.raw_actualLanguage.shim])}>{this.numberToWords("language",this.state.suburb.language[preferences.raw_actualLanguage.shim])}</span> your preference was
                          &nbsp;{this.numberToRanking(preferences.language)}&nbsp;
                        </li>

                      }

                      {preferences.raw_uni &&
                       <li> University distance <span className="badge badge-pill badge-info">{"approx. " + this.state.suburb.university_distances[preferences.raw_uni.shim].number.toFixed(2) + " km distance"}</span> your university was {preferences.raw_uni.name}</li>}
                    </ul>

                    <br/>

                    <h3>Statistics ({this.getStatFromArray(this.state.suburb.stats,"suburb-residents").year})</h3>

                    <div className="stats-section">
                    <div className='row'>
                      <div className="col-md-6">
                      <img className="stat-image" src="/otherimages/suburb-resident.png" alt="Population" height="50" width="50" />
                     <h4> Population </h4>

                      </div>
                      <div className="col-md-4">
                    {this.getStatFromArray(this.state.suburb.stats,"suburb-residents").number}
                      </div>
                    </div>

                       <div className='row'>
                      <div className="col-md-6">
                      <img className="stat-image" src="/otherimages/total-int-student-per-suburbt.png" alt="International student population" height="50" width="50" />
                      <h4> International student population </h4>

                      </div>
                      <div className="col-md-4">
                    {this.getStatFromArray(this.state.suburb.stats,"total-int-students-per-suburb").number}
                    ({(parseInt(this.getStatFromArray(this.state.suburb.stats,"total-int-students-per-suburb").number,10) * 100 /parseInt(this.getStatFromArray(this.state.suburb.stats,"suburb-residents").number),10).toFixed(2)} %)
                      </div>
                    </div>

                       <div className='row'>
                      <div className="col-md-6">
                      <img className="stat-image" src="/otherimages/offences-per-10000-population.png" alt="Crime per 10000 population" height="50" width="50" />
                      <h4> Number of crimes per 10'000 people </h4>

                      </div>
                      <div className="col-md-4">
                    {this.getStatFromArray(this.state.suburb.stats,"offences-per-10000-population").number}
                      </div>
                    </div>

                       <div className='row'>
                      <div className="col-md-6">
                      <img className="stat-image" src="/otherimages/suburb-most-common-expense-tier.png" alt="Average rental range" height="50" width="50" />
                      <h4> Most common rental price range (per week) </h4>

                      </div>
                      <div className="col-md-4">
                    {this.getStatFromArray(this.state.suburb.stats,"suburb-most-common-expense-tier").number}
                      </div>
                    </div>

                       <div className='row'>
                      <div className="col-md-6">
                      <img className="stat-image" src="/otherimages/suburb-most-int-student-lang.png" alt="Most popular language" height="50" width="50" />
                      <h4> Most popular international student language </h4>

                      </div>
                      <div className="col-md-4">
                    {this.getStatFromArray(this.state.suburb.stats,"suburb-most-int-student-lang").number}
                      </div>
                    </div>
                    </div>

                    <br/>

                    <h3>Search for properties in this area here</h3>
                    <div className="realestate-section">
                    <span>
                      <a target="_blank" href={"https://www.domain.com.au/rent/?terms=" + this.state.suburb.name.toLowerCase() + " vic"}><img alt="Domain.com.au" style={{height: '40px'}} src="/externallogos/domain.gif" /></a>
                    </span>
                    <span>
                      <a target="_blank" href={"https://www.realestate.com.au/rent/in-" + this.state.suburb.name.toLowerCase() + ",+vic/list-1"}><img alt="Realestate.com.au" style={{height:"40px"}} src="/externallogos/realestate.png" /></a>
                    </span>
                    </div>
                    <br/>


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



                    {this.state.suburb &&
                      <Map style={{'height':500+'px','width':100+'%'}} bounds={this.state.bounds}>

                            <TileLayer
                              attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <GeoJSON key={this.state.suburb.shim} data={this.state.suburb.geojson} style={this.getStyle} />
                            {this.state.uni_coords &&
                            <Marker position={this.state.uni_coords}>
                              <Popup>
                                <span>
                                  {preferences.raw_uni.name}
                                </span>
                              </Popup>
                            </Marker>}

                        </Map>
                    }
                    </div>
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
