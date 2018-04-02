import React, { Component } from 'react';
// import logo from './logo.svg';
import './Home.css';

console.log("D");

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
      <header>
        <div class="header-content">
          <div class="header-content-inner text-xs-center">
              <h1>Starting a new life in Victoria?</h1>
              <p class="lead">
                  We've got you covered
              </p>
              <p class="lead">
                  <a href="/shiny/" class="btn btn-primary btn-lg">Find a safe <i class="fas fa-home"></i></a>
              </p>
          </div>
        </div>
      </header>
      <main role="main">
            <div class="container">

                <div class="row featurette">
                    <div class="col-md-7">
                    <h2 class="featurette-heading">Umm, what is sheltr? <span class="text-muted"></span></h2>
                    <p class="lead">Our goal is to connect new students coming to Victoria with safe, affordable, and comfortable homes.</p>
                    <p class="lead">We are a diverse state. Do you like parks? Do you like hip bars? Or do you just wanna quiet suburb? We're here to help.</p>
                    </div>
                    <div class="col-md-5">
                    <img class="featurette-image img-fluid mx-auto" alt="Australia" style={{width: 350 + 'px' }} src="images/australia.png" data-holder-rendered="true" />
                    </div>
                </div>

                <div class="row featurette" id="open-data">
                    <div class="col-md-5">
                        <div class="row">
                            <div class="col-md">
                                <img src="images/data-vic.jpg" />
                            </div>
                            <div class="col-md">
                                <img src="images/data-melb.jpg" />
                            </div>
                            <div class="col-md">
                                <img src="images/crime-stats-vic.jpg" />
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md">
                                <img src="images/abs.jpg" />
                            </div>
                            <div class="col-md">
                                <img src="images/ptv.jpg" />
                            </div>
                            <div class="col-md">
                                <img src="images/vic.png" />
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <img src="images/australiangov.png" />
                            </div>
                            <div class="col-md-4">
                                <img src="images/vicroads.jpg" />
                            </div>
                        </div>
                    </div>

                    <div class="col-md-7">
                        <h2 class="featurette-heading">...but how does it work?</h2>
                        <p class="lead">Victoria is a digital state.</p>
                        <p class="lead">We've gathered, analysed, mined, and messed with loads of open data made available from the Victorian government to present an interactive visualisation for your benefit.</p>
                        <p>

                        </p>
                    </div>

                </div>

                <div class="row featurette" id="people">
                    <div class="col-md-7">
                        <h2 class="featurette-heading">..and who made this?</h2>
                        <p class="lead">We're four students at Monash University.</p>
                        <p class="lead">Pls send food. We're very hungry.</p>
                    </div>
                    <div class="col-md-4">
                        <div class="row">
                            <div class="col-md">
                                <img src="images/chinto.jpg" />
                            </div>
                            <div class="col-md">
                                <img src="images/james.jpg" />
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md">
                                <img src="images/sharmeen.jpg" />
                            </div>
                            <div class="col-md">
                                <img src="images/wanping.jpg" />
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
