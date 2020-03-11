import React, { Component } from "react";
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'
import InputGroup from 'react-bootstrap/InputGroup'
import Card from 'react-bootstrap/Card'
import axios from "axios"


class App extends Component {
    constructor(props){
        super(props);
        this.state = {query: '', responses: [], time: '', size: '', display: false};
        this.handleChange = this.handleChange.bind(this);

    }
    handleChange(event, key) {
        this.setState({[key]: event.target.value})
    }
    handleKeyPress = (event) => {
        if(event.key === 'Enter'){
            this._getQuery()
        }
    }
    _getQuery = () => {
        console.log(this.state.query)
        var self = this;
        axios.get("http://127.0.0.1:5000/" + this.state.query).then(function(response){
                                                                    self.setState({responses: response['data'][self.state.query]})
                                                                    self.setState({time: response['data']['time']})
                                                                    self.setState({size: response['data']['len']})
                                                                    self.setState({display: true})
                                                                    })
    }
    _getMoreQuery = () => {
        console.log(this.state.query)
        var self = this;
        axios.get("http://127.0.0.1:5000/next/50").then(function(response){
                                                                    var temp = self.state.responses
                                                                    console.log(self.state.responses)
                                                                    for (var i in response['data']['data']){
                                                                        temp.push(response['data']['data'][i])
                                                                    }
                                                        
                                                                    self.setState({responses: temp})
                                                                    })
    }
    createList = () => {
            let list = []
            if (this.state.display){
                list.push(
                          <div style = {{height: 60}}>
                          <Card>
                          <Card.Body>
                          <h1 style = {{fontSize: 15, paddingLeft: 13, color: 'gray'}}>About {this.state.size} results ({this.state.time} seconds)</h1>
                          
                          </Card.Body>
                          </Card>
                          </div>
            
                )
            }
        
            // Outer loop to create parent
        this.state.responses.map((r) =>{
                //Inner loop to create children
                                 
                list.push(
                
                              <div>
                                    <Card>
                                        <Card.Body>
                                            <Button variant="link" href= {r} target="_blank">
                                            {r}
                                            </Button>
                                            
                                        </Card.Body>
                                    </Card>
                              </div>);
                                 });
                                 
        
                //Create the parent and add the children
            return list
    }
        
        
    
render(){

    
    
  return (
          <div>
            <div className = "Rooms-header">
          {
          
//          <img src={ require('./Google.png') } style = {{height: 60}} />
          }
          <h1 className = "Google" style = {{color: 'blue', paddingLeft: 10}}>F</h1>
          <h1 className = "Google" style = {{color: 'red'}}>a</h1>
          <h1 className = "Google" style = {{color: 'orange'}}>b</h1>
          <h1 className = "Google" style = {{color: 'blue'}}>5</h1>
          <h1 className = "Google" style = {{color: 'brown', paddingRight: 10}}></h1>
          
          <input className = "Search" placeholder ="Search" value = {this.state.query} onKeyPress={this.handleKeyPress} onChange={event => this.handleChange(event, 'query')}
/>
          <Button onClick={() => {this._getQuery()}} variant = "outline-light"><img src={require('./magnifyingGlass.png')} className= "Magnify" /></Button>

          

            </div>
          
          {this.createList()}
          <div className = "More">
          {this.state.display && <Button className = "More" variant = "light" onClick={() => {this._getMoreQuery()}}>Show More</Button>}
          </div>

          
          </div>
          
          
  );
}
}

export default App;
