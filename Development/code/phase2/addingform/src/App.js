import React, { useState } from "react";
import "./App.css"


function App() {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [total, setTotal] = useState(0);

  const handleSubmit = (event) => {
    event.preventDefault();
    setTotal(Number(num1) + Number(num2));
  };

  return (
    <div className="add">
      <h1>Adding Two Numbers</h1>
      <br></br>
      <form 
      // onSubmit={handleSubmit}
      >
        <label>
          First Number:
          <input
            type="number"
            value={num1}
            onChange={(event) => setNum1(event.target.value)}
          />
        </label>
        <br />
        <label>
          Second Number:
          <input
            type="number"
            value={num2}
            onChange={(event) => setNum2(event.target.value)}
          />
        </label>
        <br />
        <button
        //  type="submit"
         onClick={handleSubmit}>Add</button>
      </form>
       <br></br>
      <p> Total: {total}</p>
    </div>
  );
}

export default App;
