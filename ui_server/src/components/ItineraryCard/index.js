import React, { useState } from 'react';

function ItineraryCard({ allDays }) {
  const [selectedDayIndex, setSelectedDayIndex] = useState(0); // Default to the first day

  const currentDay = allDays[selectedDayIndex];

  if (!currentDay) {
    return null; // Or a placeholder if no days are available
  }

  return (
    <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl mb-4">
      <div className="flex flex-wrap gap-2 mb-4 border-b pb-2">
        {allDays.map((day, index) => (
          <button
            key={index}
            onClick={() => setSelectedDayIndex(index)}
            className={`px-4 py-2 rounded-lg text-sm font-semibold transition-colors duration-200
              ${selectedDayIndex === index
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
          >
            Day {index + 1}
          </button>
        ))}
      </div>

      <h3 className="text-lg font-bold text-gray-800 mb-3">{currentDay.date}</h3>
      <div className="space-y-3">
        {currentDay.activities.map((activity, index) => (
          <div key={index} className="flex items-start">
            {activity.time && <p className="text-gray-500 text-sm w-20 flex-shrink-0">{activity.time}</p>}
            <p className="text-gray-700 text-sm ml-4">{activity.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ItineraryCard;
