import React, { Component } from 'react';
import { Link, Redirect } from "react-router-dom";
import { HashLink } from 'react-router-hash-link';
import './Home.css';
import detective from '../../files/detective.svg';
import chat from '../../files/chat.svg';
import credit_card from '../../files/credit_card.svg';
import university from '../../files/university.svg';
// import SpiderChart from '../spiderchart/SpiderChart';
import Select from 'react-select';
import 'react-select/dist/react-select.css';

class Home extends Component {

  constructor(props) {
    super(props);
    this.state = {
      crimeSafety: '',
      affordability: '',
      language: '',
      actualLanguage: '',
      uni: '',
      uniCampus: ''
    };

    this.onSubmit = this.onSubmit.bind(this);
  }

  handleSelectChange = function(name) {
    return function(newValue) {
        if(newValue){
        this.setState({[name]:newValue.value});
        }
        else{
        this.setState({[name]:''});
        }
    }.bind(this);
  };

  onSubmit = function(e) {
    e.preventDefault();



  }

  render() {
    const { crimeSafety, affordability, language, actualLanguage, uni, uniCampus } = this.state;

    return (
      <div>
      <div className="header-container">
        <div className="header-content">
          <div className="header-content-inner text-xs-center">
              <h1><span className="before-vicmap">are you coming to study in victoria?</span></h1>
              <div className="lead">
                we'll help with the house hunt, just help us answer a few questions!
              </div>


              <form onSubmit={this.onSubmit}>
              <div className="lead">
                  <div className="lead-row">
                  <img src={detective} alt="safety"/>
                  <div className="input-label"> safety from crime is:</div>

                  <Select className = "react-select"
                    name="crimeSafety"
                    value={crimeSafety}
                    onChange={this.handleSelectChange('crimeSafety')}
                    options={[
                      { value: null, label: 'not important' },
                      { value: '4',  label: 'very important' },
                      { value: '3',  label: 'moderately important' },
                      { value: '2',  label: 'important' },
                      { value: '1',  label: 'not important' }
                    ]}
                  />
                  </div>
                  <div className="lead-row">
                  <img src={credit_card} alt="affordability"/>
                  <div className="input-label">rental affordability is:</div>
                  <Select className = "react-select"
                    name="affordability"
                    value={affordability}
                    onChange={this.handleSelectChange('affordability')}
                    options={[
                      { value: null, label: 'not important' },
                      { value: '4',  label: 'very important' },
                      { value: '3',  label: 'moderately important' },
                      { value: '2',  label: 'important' },
                      { value: '1',  label: 'not important' }
                    ]}
                  />
                  </div>
                  <div className="lead-row">
                  <img src={chat} alt="language"/>
                  <div className="input-label"> my native language is:</div>
                  <Select className = "react-select"
                    name="language"
                    value={language}
                    onChange={this.handleSelectChange('language')}
                    options={[
                      { value: null, label: 'not important' },
                      { value: '4',  label: 'very important' },
                      { value: '3',  label: 'moderately important' },
                      { value: '2',  label: 'important' },
                      { value: '1',  label: 'not important' }
                    ]}
                  />
                  </div>
                  { language &&
                  <div className="lead-row">
                  <div className="fake-img">&nbsp;</div>
                  <div className="input-label">and it is:</div>
                  <Select
                  className = "react-select"
                      name="actualLanguage"
                      value={actualLanguage}
                      onChange={this.handleSelectChange('actualLanguage')}
                      options={[
                        { value: 'mongolian', label: 'mongolian' },
                        { value: 'russian',   label: 'russian' }
                      ]}
                    />
                  </div>
                  }
                  <div className="lead-row">
                  <img src={university} alt="university"/>
                  <div className="input-label">my preferred uni is:</div>
                  <Select
                  className = "react-select"
                      name="uni"
                      value={uni}
                      onChange={this.handleSelectChange('uni')}
                      options={[
                        { value: 'monash', label: 'monash' },
                        { value: 'rmit', label: 'rmit' }
                      ]}
                    />
                  </div>
                  { uni &&
                  <div className="lead-row">
                  <div className="fake-img">&nbsp;</div>
                  <div className="input-label">located  at:</div>
                  <Select
                  className = "react-select"
                      name="uniCampus"
                      value={uniCampus}
                      onChange={this.handleSelectChange('uniCampus')}
                      options={[
                        { value: 'caulfield', label: 'caulfield' },
                        { value: 'clayton', label: 'clayton' }
                      ]}
                    />
                  </div>
                  }
              </div>

              <button className="btn-pulsating btn btn-light btn-lg" type="submit">Submit</button>

              </form>


              <div className="lead" style={{overflow: 'auto'}}>
                {/* <Link to="/map" className="btn-pulsating btn btn-light btn-lg">click here to start! <i className="fas fa-arrow-alt-circle-right"></i></Link> */}

              </div>
          </div>
        </div>
      </div>
      <div id="about"></div>
      <main role="main">
        <div className="container home-container">
          <div className="row">
            <div className="col-md-4">
                <h2 className="featurette-heading"><HashLink smooth to="/#about" scroll={el => el.scrollIntoView({ behavior: "smooth", block: 'start' })}> * </HashLink>what is this? <span className="text-muted"></span></h2>
                  <div className="lead">Our goal is to impart local area knowledge on new students arriving in Victoria. We aim to connect you with safe, affordable, and comfortable places to live.</div>
                  <img className="featurette-image img-fluid mx-auto" alt="Travelers" style={{width: 350 + 'px' }} src="images/airport.jpg" data-holder-rendered="true" />
                  <div className="lead">We are a diverse state. Do you like parks? Do you like hip bars? Or do you just want a quiet place to study? We're here to help.</div>
            </div>
            <div className="col-md-4">
                 <h2 className="featurette-heading">how does it work?</h2>
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
                <h2 className="featurette-heading">who made this?</h2>
                <div className="lead">We're four students at Monash University.</div>
                <div className="lead">Please send food. We're very hungry. Accepting unsolicited pizza & coffee deliveries to Floor 3, Building B, Monash Caulfield.</div>
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

export default Home;
