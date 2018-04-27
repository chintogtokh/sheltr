import React, { Component } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import Select from 'react-select';
import { browseActions } from '../../actions';
import { connect } from 'react-redux';
// import {debounce} from 'lodash';

//images
import detective from '../../files/detective.svg';
import chat from '../../files/chat.svg';
import credit_card from '../../files/credit_card.svg';
import university from '../../files/university.svg';
//css
import 'react-select/dist/react-select.css';
import './Home.css';

class Home extends Component {


  mustSubmitNotification = () => toast("You must input at least one preference!",
      {
        type: toast.TYPE.INFO,
        autoClose: 5000,
        hideProgressBar: true,
        bodyClassName: "custom-toast"
      });

  constructor(props) {
    super(props);

    this.state = {};

    this.onSubmit = this.onSubmit.bind(this);
    this.getLanguages = this.getLanguages.bind(this);
    this.getUnis = this.getUnis.bind(this);
  }

  componentDidMount = function() {
    document.title = "Sheltr | Home";

    // console.log(this.props.preferences);

    if(!(Object.keys(this.props.preferences).length === 0 && this.props.preferences.constructor === Object)){
      this.setState(this.props.preferences);
    }
  }

  new = true;

  handleSelectChange = function(name) {
    return function(newValue) {
        if((typeof newValue !== "undefined" && newValue !== null) && name !== "actualLanguage" && name !== "uni"){
          this.setState({[name]:newValue.value});
          if(name==="language" && newValue.value==0){
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

  onSubmit = function(e) {
    e.preventDefault();
    this.new = false;

    let params = this.state;
    // for(var key in params){
    //   if (params[key]==="" || params[key]===null){
    //     delete params[key];
    //   }
    // }

    if(Object.keys(params).length===0){
      this.mustSubmitNotification();
    }
    else{

    const { dispatch } = this.props;
    dispatch(browseActions.enterPreferences(params));
    }
  }



  componentWillReceiveProps(nextProps) {



    if (nextProps.preferences && this.new === false) {
      this.props.history.push('/suburb');
    }
  }

  getLanguages (input) {
    if (!input) {
      if(this.state.raw_actualLanguage){
        input = this.state.raw_actualLanguage.name;
      }
        else{
          return Promise.resolve({ options: [] });
        }
    }

    return fetch(`/api/search/languages?q=${input}`)
    .then((response) => response.json())
    .then((json) => {
      return { options:json };
    });
  }

  getUnis (input) {
    if (!input) {
      if(this.state.raw_uni){
        console.log("D");
        input = this.state.raw_uni.name;
      }
        else{
          return Promise.resolve({ options: [] });
        }
    }

    return fetch(`/api/search/universities?q=${input}`)
    .then((response) => response.json())
    .then((json) => {
      return { options:json };
    });
  }

  render() {
    const { crimeSafety, affordability, language, actualLanguage, uni } = this.state;

    return (
      <div>
      <ToastContainer />
      <div className="header-container">
        <div className="header-content">
          <div className="header-content-inner text-xs-center">
              <h1><span className="before-vicmap">Welcome students, Are you coming to study in victoria?</span></h1>
              <div className="lead">
                Are you worried about finding a place to live? We'll help you. Just tell us your priorities.
              </div>
              <br/>

              <form onSubmit={this.onSubmit}>
              <div className="lead">
                  <div className="lead-row">
                  <img src={detective} alt="safety"/>
                  <div className="input-label"> Is living in a safe suburb a priority for you? </div>

                  <Select className = "react-select"
                    name="crimeSafety"
                    placeholder = ""
                    searchable = {false}
                    value={crimeSafety}
                    onChange={this.handleSelectChange('crimeSafety')}
                    options={[
                      { value: '0', label: 'Not a priority' },
                      { value: '1',  label: 'Low priority' },
                      { value: '4',  label: 'Neutral' },
                      { value: '7',  label: 'Moderate priority' },
                      { value: '10',  label: 'High priority' }
                    ]}
                  />
                  </div>
                  <div className="lead-row">
                  <img src={credit_card} alt="affordability"/>
                  <div className="input-label"> Is living in an affordable suburb a priority for you? </div>
                  <Select className = "react-select"
                    name="affordability"
                    placeholder = ""
                    value={affordability}
                    searchable = {false}
                    onChange={this.handleSelectChange('affordability')}
                    options={[
                      { value: '0', label: 'Not a priority' },
                      { value: '1',  label: 'Low priority' },
                      { value: '4',  label: 'Neutral' },
                      { value: '7',  label: 'Moderate priority' },
                      { value: '10',  label: 'High priority' }
                    ]}
                  />
                  </div>
                  <div className="lead-row">
                  <img src={chat} alt="language"/>
                  <div className="input-label"> Is living near people speaking your native language a priority for you? </div>
                  <Select className = "react-select"
                    name="language"
                    placeholder = ""
                    searchable = {false}
                    value={language}
                    onChange={this.handleSelectChange('language')}
                    options={[
                  { value: '0', label: 'Not a priority' },
                      { value: '1',  label: 'Low priority' },
                      { value: '4',  label: 'Neutral' },
                      { value: '7',  label: 'Moderate priority' },
                      { value: '10',  label: 'High priority' }
                    ]}
                  />
                  </div>
                  { (language && language!=0) &&
                  <div className="lead-row">
                  <div className="fake-img">&nbsp;</div>
                  <div className="input-label">My native language is:</div>

                  <Select.Async
                  placeholder = ""
                  name="actualLanguage"
                  autoload = {true}
                  className = "react-select"
                  value={actualLanguage}
                  valueKey="shim"
                  labelKey="name"
                  onChange={this.handleSelectChange('actualLanguage')}
                  loadOptions={this.getLanguages}
                  backspaceRemoves={true} />

                  </div>
                  }
                  <div className="lead-row">
                  <img src={university} alt="university"/>
                  <div className="input-label">My preferred university or institute is:</div>
                  <Select.Async
                  placeholder = ""
                  autoload = {true}
                  name="uni"
                  className = "react-select"
                  value={uni}
                  valueKey="shim"
                  labelKey="name"
                  onChange={this.handleSelectChange('uni')}
                  loadOptions={this.getUnis}
                  backspaceRemoves={true} />
                  </div>
              </div>

              <br/>

              <div style={{textAlign:'center'}}>
              <button className="btn btn-info btn-lg" type="submit"> Find suburbs </button>
              </div>
              </form>
          </div>
        </div>
      </div>
      <div id="about"></div>
      <main role="main">
        <div className="container home-container">
          <div className="row">
            <div className="col-md-4">
                <h2 className="featurette-heading">What is this? <span className="text-muted"></span></h2>
                  <div className="lead">Our goal is to impart local area knowledge on new students arriving in Victoria. We aim to connect you with safe, affordable, and comfortable places to live.</div>
                  <img className="featurette-image img-fluid mx-auto" alt="Travelers" style={{width: 350 + 'px' }} src="images/airport.jpg" data-holder-rendered="true" />
           </div>
            <div className="col-md-4">
                 <h2 className="featurette-heading">How does it work?</h2>
                  <div className="lead">Victoria is a world leader in open data.</div>
                  <div className="lead">We've gathered, analysed, mined, and crunched a tonne of this data to present our findings to you.</div>
                  <p className="block-of-images">
                  <a href="https://www.data.vic.gov.au" rel="noopener noreferrer" target="_blank"><img alt="Victoria's open data directory" src="images/data-vic.jpg" /></a>
                  <a href="https://data.melbourne.vic.gov.au" rel="noopener noreferrer" target="_blank"><img alt="The City of Melbourne’s open data platform" src="images/data-melb.jpg" /></a>
                  <a href="https://www.crimestatistics.vic.gov.au" rel="noopener noreferrer" target="_blank"><img alt="Crime Statistics Agency Victoria" src="images/crime-stats-vic.jpg" /></a>
                  <a href="http://www.abs.gov.au" rel="noopener noreferrer" target="_blank"><img alt="Australian Bureau of Statistics" src="images/abs.jpg" /></a>
                  <a href="https://www.ptv.vic.gov.au" rel="noopener noreferrer" target="_blank"><img alt="Public Transport Victoria" src="images/ptv.jpg" /></a>
                  <a href="https://www.vic.gov.au" rel="noopener noreferrer" target="_blank"><img alt="Victorian Government" src="images/vic.png" /></a>
                  <a href="https://www.australia.gov.au/about-australia/facts-and-figures/statistics" rel="noopener noreferrer" target="_blank"><img alt="Australian Government" src="images/australiangov.png" /></a>
                  <a href="https://www.vicroads.vic.gov.au" rel="noopener noreferrer" target="_blank"><img alt="Vicroads" src="images/vicroads.jpg" /></a>
                  </p>
            </div>
            <div className="col-md-4">
                <h2 className="featurette-heading">Who made this?</h2>
                <div className="lead">We're four students at Monash University.</div>
                <div className="lead">Floor 3, Building B, Monash Caulfield.</div>
                <p className="block-of-portraits">
                <img alt="Chintogtokh" src="images/chinto.jpg" />
                <img alt="James" src="images/james.jpg" />
                <img alt="Sharmeen" src="images/sharmeen.jpg" />
                <img alt="Wanping" src="images/wanping.jpg" />
                </p>
            </div>
          </div>
        </div>
      </main>
    </div>
    );
  }
}

function mapStateToProps(state) {
    const preferences = state.browse;
    return {
        preferences
    };
}

export default connect(mapStateToProps)(Home);
