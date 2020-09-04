import React from 'react';
import './App.css';
//import {Nav,Navbar,NavDropdown} from 'react-bootstrap';
import Menu from './components/Menu'
import {BrowserRouter} from 'react-router-dom'


function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <Menu />
    </div>
    </BrowserRouter>
  );
}

export default App;
