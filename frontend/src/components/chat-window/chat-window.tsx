import React, { useState, useEffect, useRef } from 'react';
import { io, Socket } from 'socket.io-client';
import './styles.css';

const ChatWindow: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [newMessage, setNewMessage] = useState<string>('');
  const socketRef = useRef<Socket>();

  useEffect(() => {
    socketRef.current = io('http://localhost:8000/chat_endpoint');
    socketRef.current.on('receive-message', (message: string) => {
      setMessages((prev) => [...prev, message]);
    });

    return () => {
      socketRef.current?.disconnect();
    };
  }, []);

  const sendMessage = () => {
    if (newMessage.trim()) {
      socketRef.current?.emit('send-message', newMessage);
      setNewMessage('');
    }
  };

  return (
    <div className="chat-window">
      <div className="messages-container">
        {messages.map((message, index) => (
          <div key={index} className="message">
            {message}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type a message"
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatWindow;