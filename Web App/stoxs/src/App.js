import React, {Component}from 'react';
import './App.css';
import Navbar from './components/Navbar'
import { BrowserRouter, Route } from 'react-router-dom'
import About from './components/about'
import Nyse from './components/nyse'
import Amex from './components/amex'
import Nasdaqc from './components/nasdaqc'
import Nasdaqg from './components/nasdaqg'



class App extends Component {
  render(){
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar />
          <Route path='/nasdaqc' component={Nasdaqc}/>
          <Route path='/nasdaqg' component={Nasdaqg}/>
          <Route path='/nyse' component={Nyse}/>
          <Route path='/amex' component={Amex}/>
          <Route path='/About' component={About}/>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
