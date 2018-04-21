import React, { Component } from 'react';
import './AllSuburbs.css';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
// import { Map, TileLayer, Marker, Popup } from 'react-leaflet';

class AllSuburbs extends Component {

  constructor(props) {
    super(props);
    // const { dispatch } = this.props;
    this.state = {
    };
  }

  componentDidMount = function() {
        document.title = "Sheltr | Recommendations";
    }

  componentWillMount() {
    let { preferences } = this.props;

    let params = JSON.parse(JSON.stringify(preferences));
//    delete params;

    delete params.raw_uni;
    delete params.raw_actualLanguage;

    if(params.uni && params.uni.shim){
      let tmp = params.uni.shim;
      delete params.uni;
      params.uni = tmp;
    }

    if(params.actualLanguage && params.actualLanguage.shim){
      let tmp = params.actualLanguage.shim;
      delete params.actualLanguage;
      params.actualLanguage = tmp;
    }

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params)
    };

      fetch('/api/ranked_suburbs',requestOptions)
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
                  this.setState({suburbs: response.data.map((item,i) =>
                <li key={i}><Link to={"/suburb/" + item.shim}>{item.name}</Link></li>)
              });
              }
          });
  }

  render() {
    // let { preferences} = this.props;
    let { suburbs } = this.state;
    // preferences = JSON.stringify(preferences);
    // console.log(suburbs);
    // suburbs = this.state.suburbs)
      return (
      <div>
          <main role="main">
            <div className="container">

                    <h1>...here are the top suburbs</h1>

                    <p>
                    According to the analysis of our data based on your preferences, we think that the suburbs that most fit your needs are as follows.
                    </p>
                    {/*preferences*/}

                    <hr/>
                    <ol>
                    {suburbs}
                    </ol>

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