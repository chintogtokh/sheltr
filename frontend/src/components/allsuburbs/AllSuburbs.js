import React, { Component } from 'react';
import './AllSuburbs.css';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';

class AllSuburbs extends Component {

  constructor(props) {
    super(props);
    this.state = {
      suburbs : {}
    }
  }

  mustSubmitNotification = (text) => toast(text,
      {
        type: toast.TYPE.INFO,
        autoClose: 5000,
        hideProgressBar: true,
        bodyClassName: "custom-toast"
      });

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
                  this.mustSubmitNotification("Could not fetch suburbs");
              }
              else{
                for (let i = 0; i < response.data.length; i++) {
                  fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + response.data[i].name + ", Victoria")
                    .then(response_wiki => response_wiki.json().then( data => ({
                        data: data,
                        status: response_wiki.status
                        })
                    ))
                    .then(response_wiki => {
                        if (true) {
                          let shel = response.data[i];
                          let wiki = response_wiki.data;

                          this.setState({ suburb: { ...this.state.suburb, [i]:  <Link to={"/suburb/" + shel.shim} className="text-dark">
                                <div className="card mb-4 box-shadow h-md-250">
                                  {response_wiki.status === 200 && wiki.thumbnail &&
                                    <div className="img-container">
                                      <img className="card-img-top" src={wiki.thumbnail.source} alt={shel.shim} />
                                    </div>
                                  }
                                  {!wiki.thumbnail &&
                                    <div className="img-container-empty">
                                      <span style={{color:'white'}}>No image available.</span>
                                    </div>
                                  }
                                  <div className="card-body">
                                    <h3 className="mb-0">
                                      {shel.name}
                                    </h3>
                                  </div>
                                </div>
                              </Link>  } });
                        }
                    });
                }
              }
          })
  }

  render() {
      return (
      <div>
          <ToastContainer />
          <main role="main">
            <div className="container">

              <nav aria-label="breadcrumb">
                <ol className="breadcrumb">
                  <li className="breadcrumb-item"><Link to="/">Home</Link></li>
                  <li className="breadcrumb-item active" aria-current="page">Suburb Suggestions</li>
                </ol>
              </nav>

              <h1>Suburbs matching your preferences</h1>

              <p>
              According to the analysis of our data based on your preferences, we think that the following suburbs may fit your needs.
              </p>
              <div>

                { this.state.suburb &&
                  <div className="row">{[...Array(8)].map((e, i) => {
                    return <div key={i} className="col-md-3">{this.state.suburb[i]}</div>
                  })}</div>
                }

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