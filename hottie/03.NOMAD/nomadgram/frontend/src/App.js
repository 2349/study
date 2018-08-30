import React from 'react';
import { Route, Link } from 'react-router-dom';

const App = () => (
  <div>
    <Header />
  </div>
);

const Header = () => (
  <header>
    <h1>My Contacts</h1>
    <ul>
      <li><Link to='/'>home</Link></li>
      <li><Link to='/contacts'>contacts</Link></li>
    </ul>
    
    <Route exact path="/" component={ Welcome } />
    <Route path="/contacts" component={ Contacts } />
  </header>
);

const Welcome = () => <h1>Welcome to the best contacts app!</h1>;

const Contacts = ({ match }) => (
  <div>
    <ul>
      <li><Link to='/contacts/a'>A</Link></li>
      <li><Link to='/contacts/b'>B</Link></li>
      <li><Link to='/contacts/c'>C</Link></li>
    </ul>

    <Route 
      exact
      path={ `${ match.path }` }
      render={() => <h3>Please select a contacts</h3>}
    />
    <Route
      path={ `${ match.path }/:contactName` }
      component={ Contact }
    />
  </div>
);

const Contact = ({ match }) => `Your friends name is ${ match.params.contactName }`;

export default App;
