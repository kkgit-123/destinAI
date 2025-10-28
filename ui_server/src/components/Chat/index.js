import React, { useState } from 'react';

const Chat = () => {
  const [message, setMessage] = useState('');
  const [conversation, setConversation] = useState([]);
  //   [
  //   { text: "Hello! How can I help you with your CAD evaluation today?", sender: 'bot' },
  //   { text: "I need to evaluate a new bracket design. Can you guide me through the process?", sender: 'user' },
  //   { text: "Certainly! First, please upload your CAD files and any relevant engineering drawings.", sender: 'bot' },
  //   { text: "Okay, I've uploaded the files. What's next?", sender: 'user' },
  //   { text: "Great! I'm now analyzing the design for potential stress points and material compatibility.", sender: 'bot' }
  // ]);

  const handleSendMessage = () => {
    if (message.trim()) {
      setConversation([...conversation, { text: message, sender: 'user' }]);
      setMessage('');
      // In a real application, you would send this message to a backend
      // and receive a response, then add the response to the conversation.
    }
  };

  return (
    <div className="flex flex-col w-full h-[95%] bg-gray-100 rounded-lg shadow-md text-xs">
      {/* Conversation Display Area (90%) */}
      <div className="flex-grow p-4 overflow-y-auto">
        {conversation.length === 0 ? (
          <div className="text-center text-gray-500">Start a conversation...</div>
        ) : (
          conversation.map((msg, index) => (
            <div
              key={index}
              className={`flex items-end mb-2 ${
                msg.sender === 'user' ? 'justify-end' : 'justify-start'
              }`}
            >
              {msg.sender !== 'user' && (
                <div className="w-8 h-8 rounded-full bg-gray-400 flex items-center justify-center text-white mr-2">
                  {/* You can replace this with an actual avatar image */}
                  A
                </div>
              )}
              <div
                className={`p-2 rounded-lg max-w-xs ${
                  msg.sender === 'user'
                    ? 'bg-blue-500 text-white'
                    : 'bg-gray-300 text-gray-800'
                }`}
              >
                {msg.text}
              </div>
              {msg.sender === 'user' && (
                <div className="w-8 h-8 rounded-full bg-blue-400 flex items-center justify-center text-white ml-2">
                  {/* You can replace this with an actual avatar image */}
                  U
                </div>
              )}
            </div>
          ))
        )}
      </div>

      {/* Input Area (10%) */}
      <div className="flex items-center p-4 bg-white border-t border-gray-200 h-1/10">
        <textarea
          className="flex-grow p-2 border border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="1"
          placeholder="Type your message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              handleSendMessage();
            }
          }}
        />
        <button
          className="ml-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          onClick={handleSendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;
