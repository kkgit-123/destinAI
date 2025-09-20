import React, { useState, useEffect } from 'react';

const testMessages = [
  "Analyzing your preferences...",
  "Generating personalized itinerary...",
  "Searching for the best deals...",
  "Optimizing travel routes...",
  "Finalizing your dream trip...",
  "Almost there!"
];

const LoaderOverlay = () => {
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
  const [messageVisible, setMessageVisible] = useState(true);

  useEffect(() => {
    const cycleMessages = setInterval(() => {
      setMessageVisible(false); // Start fading out current message
      setTimeout(() => {
        setCurrentMessageIndex((prevIndex) => (prevIndex + 1) % testMessages.length);
        setMessageVisible(true); // Fade in new message
      }, 700); // Duration of fade-out animation
    }, 2000); // Time each message is displayed

    return () => clearInterval(cycleMessages);
  }, []);

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-white bg-opacity-80 backdrop-blur-md">
      <div className="text-center text-gray-800 text-2xl font-bold overflow-hidden h-12 flex items-center justify-center">
        <p
          key={currentMessageIndex} // Key change forces re-render and re-triggers animation
          className={`transition-all duration-700 ease-out ${
            messageVisible ? 'transform translate-y-0 opacity-100' : 'transform translate-y-full opacity-0'
          }`}
        >
          {testMessages[currentMessageIndex]}
        </p>
      </div>
    </div>
  );
};

export default LoaderOverlay;
