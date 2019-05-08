import React from 'react';

import './input.css';

export default class ConsoleInput extends React.Component {
  
  defaultValue = "> ";
  state = {
    value: this.defaultValue
  }

  onChange = (value) => {
    if(value.length > 1 && value.substr(0, 2) === this.defaultValue){this.setState({value})}
  }

  send = (e) => {
    if(e.which === 13){
      this.props.sendQuery(e.target.value.substr(2));
      this.setState({value: this.defaultValue});
    }
  } 

  render = () => (
    <div className="console-input">
      <input 
        type="text" 
        onKeyPress={(e) => this.send(e)}
        onChange={(e) => this.onChange(e.target.value)} 
        value={this.state.value}
      />
    </div>
  );
}