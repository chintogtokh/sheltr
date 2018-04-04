import React, { Component } from 'react';
import { Link } from "react-router-dom";
import './Home.css';

class Home extends Component {

  state = {
    users:[]
  }

  // componentDidMount() {
  //   fetch('/users')
  //   .then(res => res.json())
  //   .then(users => this.setState({users}));
  // }

  render() {
    return (
      <div>
      <div className="header-container">
        <div className="header-content">
          <div className="header-content-inner text-xs-center">
              <h1><span className="before-vicmap">Starting a new life in </span><span className="vicmap">Victoria</span>?</h1>
              <p className="lead">
                We've got you covered!
              </p>
              <p className="lead">
                  I want to find a <input type="text" placeholder="relatively"/> safe suburb to live in,
                  <br /> costing <input type="text" placeholder="$100 to 200"/> per week
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
            <div className="container">

                <div className="row featurette">
                    <div className="col-lg-7 col-md-12">
                    <h2 className="featurette-heading">Umm, what is sheltr? <span className="text-muted"></span></h2>
                    <p className="lead">Our goal is to connect new students coming to Victoria with safe, affordable, and comfortable homes.</p>
                    <p className="lead">We are a diverse state. Do you like parks? Do you like hip bars? Or do you just want a quiet place to study? We're here to help.</p>
                    </div>
                    <div className="col-md-5 d-none d-lg-block">
                      <img className="featurette-image img-fluid mx-auto" alt="Travelers" style={{width: 350 + 'px' }} src="images/airport.jpg" data-holder-rendered="true" />
                    </div>
                </div>

                <div className="row featurette" id="open-data">
                    <div className="col-md-5 d-none d-lg-block">
                        <div className="row">
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/data-vic.jpg" />
                            </div>
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/data-melb.jpg" />
                            </div>
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/crime-stats-vic.jpg" />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/abs.jpg" />
                            </div>
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/ptv.jpg" />
                            </div>
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/vic.png" />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-4">
                                <img alt="Apparently this is needed" src="images/australiangov.png" />
                            </div>
                            <div className="col-md-4">
                                <img alt="Apparently this is needed" src="images/vicroads.jpg" />
                            </div>
                        </div>
                    </div>

                    <div className="col-lg-7 col-md-12">
                        <h2 className="featurette-heading">...but how does it work?</h2>
                        <p className="lead">Victoria is a world leader in open data.</p>
                        <p className="lead">We've gathered, analysed, mined, and crunched a ton of this data to present to you our findings.</p>
                        <p>

                        </p>
                    </div>

                </div>

                <div className="row featurette" id="people">
                    <div className="col-lg-7 col-md-12">
                        <h2 className="featurette-heading">..and who made this?</h2>
                        <p className="lead">We're four students at Monash University.</p>
                        <p className="lead">Please send food. We're very hungry. Accepting deliveries to Floor 3, Building B, Monash Caulfield.</p>
                    </div>
                    <div className="col-md-4 d-none d-lg-block">
                        <div className="row">
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/chinto.jpg" />
                            </div>
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/james.jpg" />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/sharmeen.jpg" />
                            </div>
                            <div className="col-md">
                                <img alt="Apparently this is needed" src="images/wanping.jpg" />
                            </div>
                        </div>
                    </div>
                </div>


            </div>
        </main>
        </div>
    );
  }
}

export default Home;
