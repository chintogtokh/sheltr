import React from "react";
import { BrowserRouter as Router,
  Route,
  Link,
  Switch } from "react-router-dom";
import './App.css';
import Navbar from "../navbar/Navbar";
import Home from "../home/Home";
import VicMap from "../vicmap/VicMap";
import Footer from "../footer/Footer";

const App = () => (
  <Router>
    <div>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/contact" component={Contact} />
        <Route exact path="/topics" component={Topics} />
        <Route exact path="/map" component={VicMap} />
        <Route exact path="/credits" component={Credits} />
        <Route component={NoMatch} />
      </Switch>
      <Footer />
    </div>
  </Router>
);

const Contact = () => (
  <div>
    <main role="main">
        <div className="container">
          <h1>Contact</h1>
          <div>
            <iframe width="100%" height="315" src="https://www.youtube.com/embed/77Ms1oCiDH4?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
          </div>
          <ul>
        <li>
          Ein
        </li>
        <li>
          Zwei
        </li>
        <li>
          Drei
        </li>
        <li>
          Vier
        </li>
        </ul>
        </div>
    </main>
  </div>
)
;
const Topics = ({ match }) => (
  <div>
  <main role="main">
        <div className="container">
    <h1>Topics</h1>
    <ul>
      <li>
        <Link to={`${match.url}/rendering`}>Rendering with React</Link>
      </li>
      <li>
        <Link to={`${match.url}/components`}>Components</Link>
      </li>
      <li>
        <Link to={`${match.url}/props-v-state`}>Props v. State</Link>
      </li>
    </ul>

    <Route path={`${match.url}/:topicId`} component={Topic} />
    <Route
      exact
      path={match.url}
      render={() => <h3>Please select a topic.</h3>}/>
  </div>
  </main>
  </div>
);

const Topic = ({ match }) => (
  <div>
  <main role="main">
        <div className="container">
    <h3>{match.params.topicId}</h3>
  </div>
  </main>
  </div>
);

const Credits = ({ location }) => (
  <div>
    <main role="main">
      <div className="container">
        <h1>Credits</h1>
        <ul>
        <li>
          Ein
        </li>
        <li>
          Zwei
        </li>
        <li>
          Drei
        </li>
        </ul>
      </div>
    </main>
  </div>
);

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