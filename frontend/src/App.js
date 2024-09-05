import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import Dashboard from './components/Dashboard/Dashboard';
import PropertyList from './components/Property/PropertyList';
import TransactionList from './components/Transaction/TransactionList';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/login" component={Login} />
                <Route path="/register" component={Register} />
                <Route path="/dashboard" component={Dashboard} />
                <Route path="/properties" component={PropertyList} />
                <Route path="/transactions" component={TransactionList} />
            </Switch>
        </Router>
    );
}

export default App;
