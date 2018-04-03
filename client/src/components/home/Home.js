import React, { Component } from 'react';
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
              <h1>Starting a new life in Victoria?</h1>
              <p className="lead">
                  We've got you covered
              </p>
              <p className="lead">
                  <a href="/map" className="btn btn-primary btn-lg">Find a safe <i className="fas fa-home"></i></a>
              </p>
          </div>
        </div>
      </div>
      <main role="main">
            <div className="container" id="about">

                <div className="row featurette">
                    <div className="col-md-7">
                    <h2 className="featurette-heading">Umm, what is sheltr? <span className="text-muted"></span></h2>
                    <p className="lead">Our goal is to connect new students coming to Victoria with safe, affordable, and comfortable homes.</p>
                    <p className="lead">We are a diverse state. Do you like parks? Do you like hip bars? Or do you just wanna quiet suburb? We're here to help.</p>
                    </div>
                    <div className="col-md-5">
                    <img className="featurette-image img-fluid mx-auto" alt="Australia" style={{width: 350 + 'px' }} src="images/australia.png" data-holder-rendered="true" />
                    </div>
                </div>

                <div className="row featurette" id="open-data">
                    <div className="col-md-5">
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

                    <div className="col-md-7">
                        <h2 className="featurette-heading">...but how does it work?</h2>
                        <p className="lead">Victoria is a digital state.</p>
                        <p className="lead">We've gathered, analysed, mined, and messed with loads of open data made available from the Victorian government to present an interactive visualisation for your benefit.</p>
                        <p>

                        </p>
                    </div>

                </div>

                <div className="row featurette" id="people">
                    <div className="col-md-7">
                        <h2 className="featurette-heading">..and who made this?</h2>
                        <p className="lead">We're four students at Monash University.</p>
                        <p className="lead">Pls send food. We're very hungry.</p>
                    </div>
                    <div className="col-md-4">
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
