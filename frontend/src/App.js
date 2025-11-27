
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  const sendMessage = async () => {
    try {
      await axios.post('http://localhost:8000/api/send-to-discord', { content: message });
      alert('Message sent!');
      setMessage('');
    } catch (error) {
      console.error('Error sending message:', error);
      alert('Failed to send message.');
    }
  };

  return (
    <div>
      <h1>Send a message to Discord</h1>
      <input 
        type="text" 
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default App;
