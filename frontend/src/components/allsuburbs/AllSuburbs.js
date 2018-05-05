import React, { Component } from 'react';
import './AllSuburbs.css';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import Select from 'react-select';

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

  handleFilterChange = function(name) {
    return function(newValue) {
        if((typeof newValue !== "undefined" && newValue !== null) && name !== "actualLanguage" && name !== "uni"){
          this.setState({[name]:newValue.value});
          if(name==="language" && newValue.value===0){
            this.setState({"actualLanguage": null});
          }
        }
        else if(typeof newValue !== "undefined"){
          this.setState({[name]:newValue,["raw_"+name]:newValue});
        }
        else{
          this.setState({[name]:''});
        }
    }.bind(this);
  };


  render() {

    const { filter } = this.state;

      return (
      <div id="AllSuburbsComponent">
          <ToastContainer />
          <main role="main">
            <div className="container">

              <nav aria-label="breadcrumb">
                <ol className="breadcrumb">
                  <li className="breadcrumb-item"><Link to="/">Home</Link></li>
                  <li className="breadcrumb-item active" aria-current="page">Suburb Suggestions</li>
                </ol>
              </nav>

              <h1>Suburb Suggestions</h1>

              <div>
                The following suburbs might fit your needs. Start drilling down using the options to the right!
              </div>

              <div className="sortable-section-container">
                <div className="sortable-section">

                  <div className="filter-text-container">
                    <div className="filter-text">
                    Sort by:
                    </div>
                  </div>
                  <Select className = "react-select"
                  name="filter"
                  placeholder = "distance"
                  value={filter}
                  searchable = {false}
                  style={{width:'150px'}}
                  onChange={this.handleFilterChange('filter')}
                  options={[
                    { value: 'safety', label: 'safety' },
                    { value: 'affordability', label: 'affordability' },
                    { value: 'distance', label: 'distance' },
                  ]}
                />
                </div>
              </div>


                { this.state.suburb &&
                  <div className="row">{[...Array(8)].map((e, i) => {
                    return <div key={i} className="col-md-3">{this.state.suburb[i]}</div>
                  })}</div>
                }
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