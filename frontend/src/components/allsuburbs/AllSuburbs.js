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
      suburb_0: "",
      suburb_1: "",
      suburb_2: "",
      suburb_3: "",
      suburb_4: "",
      suburb_5: "",
      suburb_6: "",
      suburb_7: "",
      suburb_8: "",
      suburb_9: ""
    };
  }

  componentDidMount = function() {
        document.title = "Sheltr | Recommendations";
    }


  getWiki = function(name,count){

    fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + name + ", Victoria")
          .then(response => response.json().then( data => ({
              data: data,
              status: response.status
              })
          ))
          .then(response => {
              if (response.status === 200) {
                  return response.data.extract;
              }
          });
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

                for (let i = 0; i < response.data.length; i++) {
                  fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + response.data[i].name + ", Victoria")
                    .then(response1 => response1.json().then( data => ({
                        data: data,
                        status: response1.status
                        })
                    ))
                    .then(response1 => {
                        if (true) {
                          let shel = response.data[i];
                          let wiki = response1.data;
                          this.setState({["suburb_" + i]:
                                        <div className="card flex-md-row mb-4 box-shadow h-md-250">
              <div className="card-body d-flex flex-column align-items-start">
                <h3 className="mb-0">
                  <Link to={"/suburb/" + shel.shim} className="text-dark">
                  {i+1}. {shel.name}
                </Link>
                </h3>
                <div className="mb-1 text-muted"></div>
                <p className="card-text mb-auto">
                  {response1.status === 200?wiki.extract:shel.name + " is a suburb in Victoria."}

                </p>
                <Link to={"/suburb/" + shel.shim}>
                  Continue Reading
                </Link>
              </div>
              {response1.status === 200 &&
              <img className="suburb-card card-img-right flex-auto d-none d-lg-block" alt="Thumbnail [200x250]" src={wiki.thumbnail.source} />}
            </div>
                        });
                        }
                    });
                }

            //     )
            //   });
              }
          })
  }

  render() {
      return (
      <div>
          <main role="main">
            <div className="container">

              <h1>...here are the top suburbs</h1>

              <p>
              According to the analysis of our data based on your preferences, we think that the suburbs that most fit your needs are as follows.
              </p>
              <div>
              {this.state.suburb_0}
              {this.state.suburb_1}
              {this.state.suburb_2}
              {this.state.suburb_3}
              {this.state.suburb_4}
              {this.state.suburb_5}
              {this.state.suburb_6}
              {this.state.suburb_7}
              {this.state.suburb_8}
              {this.state.suburb_9}
              </div>
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