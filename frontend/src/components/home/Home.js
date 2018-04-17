import React, { Component } from 'react';
import { Link } from "react-router-dom";
import './Home.css';
// import SpiderChart from '../spiderchart/SpiderChart';

class Home extends Component {

  render() {
    return (
      <div>
      <div className="header-container">
        <div className="header-content">
          <div className="header-content-inner text-xs-center">
              <h1><span className="before-vicmap">are you starting a new life in </span><span className="vicmap">victoria</span>?</h1>
              <p className="lead">
                we'll help with the house hunt, just help us answer a few questions!
              </p>
              <p className="lead">
                  I consider:
                  <br/>
                  <i className="fas fa-eye"></i> safety from crime to be:
                  <select name="safety">
                    <option value>irrelevant</option>
                    <option value="1">very important</option>
                    <option value="2">moderately important</option>
                    <option value="3">not important</option>
                  </select>
                  <br />
                  <i className="fas fa-money-bill-alt"></i> affordability to be:
                  <select name="affordability">
                    <option value>irrelevant</option>
                    <option value="1">very important</option>
                    <option value="2">moderately important</option>
                    <option value="3">not important</option>
                  </select>
                  <br />
                  <i className="fas fa-language"></i> my native language to be:
                  <select name="language">
                    <option value>irrelevant</option>
                    <option value="1">very important</option>
                    <option value="2">moderately important</option>
                    <option value="3">not important</option>
                  </select> and my language is
                  <select name="spoken-language">
                    <option value="3">mongolian</option>
                    <option value="3">russian</option>
                  </select>
                  <br />
                  <i className="fas fa-university"></i> my preferred uni to be:
                  <select name="uni">
                    <option value>monash caulfield</option>
                    <option value>monash clayton</option>
                    <option value>rmit</option>
                  </select>
                  <br />
              </p>
              <p className="lead">
                <Link to="/map" className="btn btn-primary btn-lg">Let's go <i className="fas fa-arrow-alt-circle-right"></i></Link>
              </p>
          </div>
        </div>
      </div>
      <div id="about"></div>
      <main role="main">
            <div className="container home-container">

            <div className="row">

              <div className="col-md-4">
                  <h2 className="featurette-heading">what is this? <span className="text-muted"></span></h2>
                    <p className="lead">Our goal is to impart local area knowledge on new students arriving in Victoria. We aim to connect you with safe, affordable, and comfortable places to live.</p>
                    <img className="featurette-image img-fluid mx-auto" alt="Travelers" style={{width: 350 + 'px' }} src="images/airport.jpg" data-holder-rendered="true" />
                    <p className="lead">We are a diverse state. Do you like parks? Do you like hip bars? Or do you just want a quiet place to study? We're here to help.</p>
              </div>
              <div className="col-md-4">
                   <h2 className="featurette-heading">how does it work?</h2>
                    <p className="lead">Victoria is a world leader in open data.</p>
                    <p className="lead">We've gathered, analysed, mined, and crunched a ton of this data to present to you our findings.</p>
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
                  <p className="lead">We're four students at Monash University.</p>
                  <p className="lead">Please send food. We're very hungry. Accepting deliveries to Floor 3, Building B, Monash Caulfield.</p>
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
