import React, { useState, useEffect, useRef } from 'react';
import './styles.css';

const ChatWindow: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [newMessage, setNewMessage] = useState<string>('');
  const socketRef = useRef<WebSocket>();

  useEffect(() => {
    // Use native WebSocket instead of Socket.io
    socketRef.current = new WebSocket('ws://localhost:8000/ws');

    socketRef.current.onmessage = (event) => {
      setMessages((prev) => [...prev, event.data]);
    };

    socketRef.current.onopen = () => {
      // If you need to send token or userId when socket opens, you can do it here.
      // Example:
      // socketRef.current?.send(JSON.stringify({ token: 'your-token', userId: 'user-id' }));
    };

    return () => {
      socketRef.current?.close();
    };
  }, []);

  const sendMessage = () => {
    if (newMessage.trim() && socketRef.current?.readyState === WebSocket.OPEN) {
      socketRef.current.send(newMessage);
      setNewMessage('');
    }
  };

  return (
    <div>
      <div className="chat-window">
        <div className="messages-container">
          {messages.map((message, index) => (
            <div key={index} className="message">
              {message}
            </div>
          ))}
        </div>
        <div className="form-control w-full">
          <label className="label">
            <span className="label-text">Send a message</span>
          </label>
          <div className="join">
            <input type="text" placeholder="I want a budget" className="input input-bordered w-full join-item" />
            <button className="btn join-item" onClick={sendMessage}>Send</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;
