import React from 'react';

import './console.css';
import Spinner from '../assets/ajax-loader.gif';

export default class Segment extends React.Component {
  state = {
    results: null
  }
  ref = React.createRef();

	componentDidUpdate(){
		this.ref.current.scrollIntoView({behavior:'smooth', block:"end"});
  }
  
  componentDidMount(){
    fetch(`/Question?Question=${this.props.search}`)
    .then(r => { 
      if(r.ok){
        return r.json();
      }
      else { throw new Error(r.statusText); }
    }).then(d => this.setState({results: d}))
    .catch(err => console.error(err));
      
    /*
    setTimeout(() => {
	  this.setState({results: [
      {score:"100", sentence:"Hello! My name is Sweq, how may I help you? Ask me anything! I know many thing."},
      {score:"100", sentence:"Hello! My name is Sweq, how may I help you? Ask me anything! I know many thing."},
      {score:"100", sentence:"Hello! My name is Sweq, how may I help you? Ask me anything! I know many thing."}
    ]});
    }, 1000);
   */
  }

  render = () => (
    <div ref={this.ref}>
      <BlockUsr text={this.props.search}/>
      {this.state.results ? (
        this.state.results.map((item, i) => <BlockKomp key={i} content={item}/>)
      ):(
        <BlockSearching/>
      )}
    </div>
  );
}

const BlockUsr = ({text}) => (
  <div className="block usr">
    <div>{text}</div>
  </div>
);

class BlockKomp extends React.Component {	
	render(){
    console.log(this.props.content);
		return (

  <div className="block komp">
    <div>
		<div>{this.props.content.sentence}</div>
	</div>
  </div>);	
	}
}

const BlockSearching = () => (
  <div className="block komp">
    <div><img src={Spinner} alt="Working on something"/></div>
  </div>
);