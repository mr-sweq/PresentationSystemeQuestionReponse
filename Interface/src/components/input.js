import React from 'react';

import './input.css';

export default class ConsoleInput extends React.Component {
  
  state = {
    value: ""
  }

  send = (e) => {
    if(e.which === 13){
      this.props.sendQuery(e.target.value);
      this.setState({value: ""});
    }
  } 

  render = () => (
    <div className="console-input">
      <div className="caret">></div>
      <div className="input">
      <input 
        type="text" 
        onKeyPress={(e) => this.send(e)}
        onChange={(e) => this.setState({value: e.target.value})} 
        placeholder="Inscrivez votre question"
        value={this.state.value}
      />
      </div>
  </div>    
  );
}