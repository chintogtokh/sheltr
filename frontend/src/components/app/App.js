import React from "react";
import { BrowserRouter as Router,
  Route,
  Switch } from "react-router-dom";
import './App.css';
// components
import Navbar from "../navbar/Navbar";
import Home from "../home/Home";
import VicMap from "../vicmap/VicMap";
import Footer from "../footer/Footer";
import Contact from "../contact/Contact";
import Auth from "../auth/Auth";
import Suburb from "../suburb/Suburb";

const App = () => (
  <Router>
    <div>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/contact" component={Contact} />
        <Route exact path="/map" component={VicMap} />
        <Route exact path="/suburb/:name" component={Suburb} />
        <Route path="/auth" component={Auth} />
        <Route component={NoMatch} />
      </Switch>
      <Footer />
    </div>
  </Router>
);


// //temporary
// const Credits = ({ location }) => (
//   <div>
//     <main role="main">
//       <div className="container">
//         <h1>Credits</h1>
//         <ul>
//         <li>
//           Ein
//         </li>
//         <li>
//           Zwei
//         </li>
//         <li>
//           Drei
//         </li>
//         </ul>
//       </div>
//     </main>
//   </div>
// );

const NoMatch = ({ location }) => (
  <div>
    <main role="main">
        <div className="container">
          <h1>Sorry :(</h1>
          <pre>No match for <code>{location.pathname}</code></pre>
        </div>
    </main>
  </div>
);


export default App;