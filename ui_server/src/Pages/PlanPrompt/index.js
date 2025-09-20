
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import ThemedHeader from '../../components/ThemedHeader'; // Import ThemedHeader
import Breadcrumbs from '../../components/Breadcrumbs';
import promptCards from '../../constants/promptCards'; // Import promptCards as fallback
import { ENDPOINTS } from '../../constants/endpoints';
import LoaderOverlay from '../../components/LoaderOverlay'; // Import LoaderOverlay

function PlanPrompt() {
  const [currentPromptCards, setCurrentPromptCards] = useState(promptCards);
  const [currentTripCards, setCurrentTripCards] = useState([]); // New state for trip cards
  const [isLoading, setIsLoading] = useState(false); // State to control loader visibility

  useEffect(() => {
    const fetchPromptCards = async () => {
      try {
        const response = await fetch(ENDPOINTS.PROMPT_CARDS);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setCurrentPromptCards(data);
      } catch (error) {
        console.error("Failed to fetch prompt cards:", error);
        alert("Failed to load prompt cards from server. Using local data.");
        setCurrentPromptCards(promptCards); // Fallback to local data
      }
    };

    const fetchTripCards = async () => {
      try {
        const response = await fetch(ENDPOINTS.TRIP_CARDS);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setCurrentTripCards(data);
      } catch (error) {
        console.error("Failed to fetch trip cards:", error);
        alert("Failed to load trip cards from server.");
        setCurrentTripCards([]); // Fallback to empty array
      }
    };

    fetchPromptCards();
    fetchTripCards(); // Fetch trip cards
  }, []);
  const navigate = useNavigate();
  const [promptText, setPromptText] = useState('');

  const handleProcessPrompt = async () => {
    setIsLoading(true); // Show loader
    try {
      const response = await fetch(ENDPOINTS.PROCESS_PROMPT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: promptText }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      const planId = data.data.id;
      navigate(`/plan/result/${planId}`);
    } catch (error) {
      console.error("Failed to process prompt:", error);
      alert("Failed to process prompt. Please try again.");
    } finally {
      setIsLoading(false); // Hide loader
    }
  };

  return (
    <div className="flex flex-col h-screen w-screen bg-gray-100">
      {/* Header */}
      <div className='flex w-screen h-[10%] mb-1'>  
            <ThemedHeader>
            <div className="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                    </svg>
                    <span className="font-bold text-lg text-gray-800">DestiniAI</span>
                </div>
            </ThemedHeader>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white shadow-md w-full h-[5%] flex items-center justify-center">
        <Breadcrumbs currentStep={1} /> {/* Assuming "Plan Prompt" is the first step */}
      </div>

      {/* Main Content Area */}
      <div className="flex flex-col flex-grow p-4 md:p-8 overflow-auto items-center">
        {/* Text area and Send button */}
        <div className="flex items-center justify-center w-full mb-8">
          <div className="relative w-[90%] md:w-[70%] lg:w-[50%] flex items-center">
            <textarea
              placeholder="Text area to add text"
              className="flex-grow border border-gray-300 rounded-full py-2 px-6 text-lg focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
              value={promptText}
              onChange={(e) => {
                setPromptText(e.target.value);
                e.target.style.height = 'auto';
                e.target.style.height = Math.min(e.target.scrollHeight, 4 * 24) + 'px'; // Assuming 24px per line height, max 4 lines
              }}
              rows="1"
              style={{ minHeight: '48px', maxHeight: '96px', overflowY: 'auto' }} // Approx 2 lines min, 4 lines max, scrollable
            ></textarea>
            <button 
              className="absolute right-1 bg-blue-500 text-white rounded-full p-2 shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
              onClick={handleProcessPrompt}
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </button>
          </div>
        </div>

        {/* Sample cards for trip planner */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mb-8 w-[90%] md:w-[70%] lg:w-[50%]">
          {currentPromptCards.map((card) => (
            <div
              key={card.id}
              className="bg-white rounded-lg shadow-md p-3 h-[100px] flex items-center justify-center text-center cursor-pointer hover:shadow-lg transition-shadow"
              onClick={() => setPromptText(card.promptText)}
            >
              <p className="text-gray-700 text-sm font-medium">{card.displayText}</p>
            </div>
          ))}
        </div>

        {/* Dynamically loaded trip cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-[90%] md:w-[70%] lg:w-[50%]">
          {currentTripCards.map((card) => (
            <div
              key={card.id}
              className="bg-white rounded-lg shadow-md cursor-pointer hover:shadow-lg transition-shadow overflow-hidden"
              onClick={() => setPromptText(card.title)} // Assuming clicking a trip card sets its title as prompt
            >
              <div className="relative h-[120px] bg-cover bg-center" style={{ backgroundImage: `url('${card.imageUrl}')` }}>
                <div className="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                  <p className="text-white font-bold text-xl ">{card.title}</p>
                </div>
              </div>
              <div className="p-4 h-[80px] flex flex-col justify-center">
                <p className="text-gray-700 text-sm text-center">{card.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
      {isLoading && <LoaderOverlay />}
    </div>
  );
}

export default PlanPrompt;
