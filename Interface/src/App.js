import React, { Component } from 'react';

import './App.css';

import ConsoleSegment from './components/console';
import ConsoleInput from './components/input';

class App extends Component {

  state = {
    searches: ["Bonjour!"]
  }
  
  addQuery = (value) => {
    let searches = this.state.searches;
    searches.push(value);
    this.setState({searches});
  };

  render() {
    return (
      <div className="console">
        <div id="main-window" className="console-container">
          <div>
            {this.state.searches.map((item, i) => <ConsoleSegment key={i} search={item}/>)}
          </div>
        </div>
        <ConsoleInput sendQuery={this.addQuery}/>
      </div>
    );
  }

}

export default App;
