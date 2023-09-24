import './App.css';
import ChatWindow from './components/chat-window/chat-window';

function App() {
  return (
    <div className="app-container">
      <div className="chat-container">
        <ChatWindow />
      </div>
      <div className="side-pane">
        <p>Side Pane Content</p>
      </div>
    </div>
  );
}

export default App;