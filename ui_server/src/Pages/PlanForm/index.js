import React, { useState } from 'react';
import ThemedHeader from '../../components/ThemedHeader'; // Import ThemedHeader
import Breadcrumbs from '../../components/Breadcrumbs';
import { useNavigate } from 'react-router-dom';
function PlanForm() {
  const [budget, setBudget] = useState(5); // Example for slider
  const [travelers, setTravelers] = useState(1); // Example for number of travelers
  const [selectedInterests, setSelectedInterests] = useState(['Adventure', 'Relax']); // Initial selected interests
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [destinations, setDestinations] = useState(['']); // For multiple destinations
  const [preferredPace, setPreferredPace] = useState('Moderate'); // For preferred pace
  const navigate = useNavigate();
  const toggleInterest = (interest) => {
    setSelectedInterests((prevInterests) =>
      prevInterests.includes(interest)
        ? prevInterests.filter((item) => item !== interest)
        : [...prevInterests, interest]
    );
  };

  const handleDestinationChange = (index, value) => {
    const newDestinations = [...destinations];
    newDestinations[index] = value;
    setDestinations(newDestinations);
  };

  const addDestination = () => {
    setDestinations([...destinations, '']);
  };

  const removeDestination = (index) => {
    const newDestinations = [...destinations];
    newDestinations.splice(index, 1);
    setDestinations(newDestinations);
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
                    <span className="font-bold text-lg text-gray-800">Trip Journey Trip</span>
                </div>
                <div className="font-bold text-lg text-gray-800">Trip Details</div>
                <div className="flex items-center">
                    <img src="https://via.placeholder.com/30" alt="User" className="rounded-full" />
                </div>
            </ThemedHeader>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white shadow-md w-full h-[5%] flex items-center justify-center">
        <Breadcrumbs currentStep={1} /> {/* Assuming "Trip Details" is the second step (index 1) */}
      </div>

      {/* Main Content */}
      <div className="flex flex-col flex-grow p-8 overflow-auto mb-3">
        <h1 className="text-lg font-bold mb-2">Let's define your journey</h1>
        <p className="text-gray-600 text-sm mb-4 w-[60%]">
          Provide key full details so let us can few guide gustim plan—or answer guidens if
          questions if ano chose Help Me Plan.
        </p>

        {/* Form Layout */}
        <div className="flex w-full h-[70%]">
          {/* Left Column */}
          <div className="flex flex-col w-[48%] mr-[2%] h-full">
            {/* Top Card */}
            <div className="flex flex-col p-4 bg-white rounded-lg shadow-md mb-4">
              <label className="block text-gray-700 text-sm font-bold mb-2">Destinations</label>
              {destinations.map((destination, index) => (
                <div key={index} className="flex items-center border border-gray-300 rounded-md p-2 mb-2">
                  <input
                    type="text"
                    placeholder="Destination"
                    value={destination}
                    onChange={(e) => handleDestinationChange(index, e.target.value)}
                    className="flex-grow outline-none"
                  />
                  {destinations.length > 1 && (
                    <button onClick={() => removeDestination(index)} className="ml-2 text-red-500">
                      &times;
                    </button>
                  )}
                </div>
              ))}
              <button onClick={addDestination} className="text-blue-600 mb-4 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clipRule="evenodd" />
                </svg>
                Add Destination
              </button>

              <div className="flex justify-between mb-4">
                <div className="w-[48%]">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
                  <input
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                    className="border border-gray-300 rounded-md p-2 w-full outline-none"
                  />
                </div>
                <div className="w-[48%]">
                  <label className="block text-gray-700 text-sm font-bold mb-2">End Date</label>
                  <input
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    className="border border-gray-300 rounded-md p-2 w-full outline-none"
                  />
                </div>
              </div>

              <label className="block text-gray-700 text-sm font-bold mb-2">Trip Type</label>
              <select className="border border-gray-300 rounded-md p-2 w-full outline-none mb-4">
                <option>Leisure</option>
                <option>Business</option>
                <option>Adventure</option>
                <option>Family</option>
              </select>
            </div>

            {/* Bottom Card */}
            <div className="flex flex-col p-4 bg-white rounded-lg shadow-md ">
              <label className="block text-gray-700 text-sm font-bold mb-2">Number of Travelers</label>
              <div className="flex items-center border border-gray-300 rounded-md p-2 mb-4 w-full">
                <button
                  onClick={() => setTravelers(Math.max(1, travelers - 1))}
                  className="p-2 border-r border-gray-300 text-gray-600 hover:bg-gray-100 rounded-l-md w-[20%]"
                >
                  -
                </button>
                <input
                  type="number"
                  value={travelers}
                  onChange={(e) => setTravelers(Number(e.target.value))}
                  className="flex-grow text-center outline-none w-[60%]"
                />
                <button
                  onClick={() => setTravelers(travelers + 1)}
                  className="p-2 border-l border-gray-300 text-gray-600 hover:bg-gray-100 rounded-r-md w-[20%]"
                >
                  +
                </button>
              </div>

              <label className="block text-gray-700 text-sm font-bold mb-2">Anything special? Dietary needs, events, or preferences....</label>
              <div className="flex items-center border border-gray-300 rounded-md p-2">
                <textarea
                  placeholder="Anything special? Dietary needs, events, or preferences...."
                  className="flex-grow outline-none resize-none h-24"
                ></textarea>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 12h.01M12 12h.01M19 12h.01" />
                </svg>
              </div>
            </div>
          </div>

          {/* Right Column */}
          <div className="flex flex-col w-[48%] p-4 bg-white rounded-lg shadow-md">
            <label className="block text-gray-700 text-sm font-bold mb-2">Budget</label>
            <div className="mb-4 relative">
              <div className="flex justify-between text-sm text-gray-600 mb-2">
                <span>₹0</span>
                <span>₹5 L</span>
              </div>
              <div className="absolute -top-7 -right-8 -translate-x-1/2 bg-blue-500 text-white text-xs px-2 py-1 rounded-md shadow-md">
                ₹{budget * 5000} {/* Assuming 10k to 5L, so 1 unit = 5000 */}
              </div>
              <input
                type="range"
                min="0"
                max="100"
                value={budget}
                onChange={(e) => setBudget(e.target.value)}
                className="w-full h-2 bg-blue-200 rounded-lg appearance-none cursor-pointer"
              />
            </div>

            <label className="block text-gray-700 text-sm font-bold mb-2">Interests / Tags</label>
            <div className="flex flex-wrap gap-2 mb-4">
              {['Adventure', 'Foodie', 'Culture', 'Relax', 'Shopping'].map((interest) => (
                <button
                  key={interest}
                  onClick={() => toggleInterest(interest)}
                  className={`px-3 py-1 rounded-full text-sm flex items-center ${
                    selectedInterests.includes(interest)
                      ? 'bg-blue-500 text-white'
                      : 'bg-gray-200 text-gray-700'
                  }`}
                >
                  {interest === 'Adventure' && (
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  )}
                  {interest}
                </button>
              ))}
            </div>

            <label className="block text-gray-700 text-sm font-bold mb-2">Preferred Pace</label>
            <div className="flex flex-wrap gap-2 mb-4">
              {['Fast-paced', 'Moderate', 'Relaxed'].map((pace) => (
                <button
                  key={pace}
                  onClick={() => setPreferredPace(pace)}
                  className={`px-3 py-1 rounded-full text-sm ${
                    preferredPace === pace
                      ? 'bg-blue-500 text-white'
                      : 'bg-gray-200 text-gray-700'
                  }`}
                >
                  {pace}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Footer Buttons */}
      <div className="flex justify-end items-center bg-white p-4 shadow-md w-full h-[8%] ">
      
        <div>
          <button className="border border-blue-500 text-blue-500 px-6 py-2 rounded-full mr-4">Back</button>
          <button className="bg-blue-500 text-white px-6 py-2 rounded-full" onClick={() => navigate('/plan/result/1')}>Generate Plan</button>
        </div>
      </div>
    </div>
  );
}

export default PlanForm;
