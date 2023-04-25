import React, { useState, useEffect } from 'react';

function Card() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3005/players')
      .then(response => response.json())
      .then(players => setPlayers(players))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      {players.map((player) => (
        <div key={player.id} className="player-card">
          <h2>{player.name}</h2>
          <p>Position: {player.position}</p>
          <p>Age: {player.age}</p>
        </div>
      ))}
    </div>
  );
}

export default Card;
