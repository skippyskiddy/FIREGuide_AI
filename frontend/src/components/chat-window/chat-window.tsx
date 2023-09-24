import React, { useState, useEffect, useRef } from 'react';
import { io, Socket } from 'socket.io-client';
import './styles.css';

const ChatWindow: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [newMessage, setNewMessage] = useState<string>('');
  const socketRef = useRef<Socket>();

  // useEffect(() => {
  //   socketRef.current = io('http://localhost:8000/ws', {
  //     query: {
  //       token: 'your-token',
  //       userId: 'user-id'
  //     }
  //   });
  //   socketRef.current.on('receive-message', (message: string) => {
  //     setMessages((prev) => [...prev, message]);
  //   });

  //   return () => {
  //     socketRef.current?.disconnect();
  //   };
  // }, []);

  const sendMessage = () => {
    if (newMessage.trim()) {
      socketRef.current?.emit('send-message', newMessage);
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