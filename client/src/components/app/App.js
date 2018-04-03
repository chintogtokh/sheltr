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
        <Route exact path="/about" component={About} />
        <Route exact path="/topics" component={Topics} />
        <Route exact path="/map" component={VicMap} />
        <Route component={NoMatch} />
      </Switch>
      <Footer />
    </div>
  </Router>
);

const About = () => (
  <main>
    <h2>About</h2>
  </main>
)
;
const Topics = ({ match }) => (
  <div>
    <h2>Topics</h2>
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
      render={() => <h3>Please select a topic.</h3>}
    />
  </div>
);

const Topic = ({ match }) => (
  <div>
    <h3>{match.params.topicId}</h3>
  </div>
);

const NoMatch = ({ location }) => (
  <div>
    <h3>
      No match for <code>{location.pathname}</code>
    </h3>
  </div>
);


export default App;