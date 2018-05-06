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

  numberToStar = function(number){

    var ret=[];
    var star=<i className="fas fa-star"></i>
    var halfStar=<i className="fas fa-star"></i>

    var rating = Math.floor(number/10);

    for(var i=0;i<Math.floor(rating/2);i++){
      ret.push(star);
    }
    if(rating%2!=0){
      ret.push(halfStar);
    }

    return [<span className="empty"><i className="far fa-star"></i><i className="far fa-star"></i><i className="far fa-star"></i><i className="far fa-star"></i><i className="far fa-star"></i>
      </span>,<span className='actual'>{ret}</span>];

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

                          this.setState({ suburb: { ...this.state.suburb, [i]:
                                <div className="card mb-4 box-shadow h-md-250">
                                  <div className="card-body">
                                    <h3 className="mb-0">
                                      <Link to={"/suburb/" + shel.shim} className="text-dark">{shel.name}</Link>
                                    </h3>
                                    <div className="card-text">
                                      <div className="star-label"> Safety </div>
                                      <div className="star-ratings">
                                        {this.numberToStar(shel.rating_safety)}
                                      </div>
                                      <br />
                                      <div className="star-label">Affordability</div>
                                      <div className="star-ratings">
                                        {this.numberToStar(shel.rating_affordability)}
                                      </div>
                                    </div>
                                  </div>
                                </div>
                                } });
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
                    University:
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


                <div className="sortable-section">

                  <div className="filter-text-container">
                    <div className="filter-text">
                    Distance:
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

                 <div className="sortable-section">

                  <div className="filter-text-container">
                    <div className="filter-text">
                    Language:
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