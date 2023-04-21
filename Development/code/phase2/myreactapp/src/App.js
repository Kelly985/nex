//import logo from './logo.svg';
import './App.css';
import React from 'react';


function welcome(){
  return <p>welcome to the cash app</p>
}

function App() {

  function handleClick() {
    alert('No cash in your Account');
  };


  return (

    <div id ='image' >
      <img id = 'cash'
      src='https://images.unsplash.com/photo-1553729459-efe14ef6055d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8bW9uZXl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60'
      alt='cash yoh'
      
      />
      <p>You've Gotta Love The Paper.</p>
      <button id = 'btn' onClick={handleClick}>
      CashButton
    </button>

<welcome/>

    </div>

    



  );
}

export default App;
