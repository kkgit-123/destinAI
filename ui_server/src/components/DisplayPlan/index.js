import React, { useState, useEffect } from "react";
import { InfinitySpin } from "react-loader-spinner";

function DisplayPlan({ planData, filteredTabs, onDayClick, MapComponent }) {
  const [activeTab, setActiveTab] = useState(filteredTabs ? filteredTabs[0] : "Overview");
  const [selectedDayIndex, setSelectedDayIndex] = useState(0); // State to manage selected day

  useEffect(() => {
    if (filteredTabs && !filteredTabs.includes(activeTab)) {
      setActiveTab(filteredTabs[0]);
    }
  }, [filteredTabs, activeTab]);

  const renderTabContent = () => {
    const contentBlocks = planData.tabContent[activeTab];
    if (!contentBlocks) return null;

    return contentBlocks.map((block, index) => {
      switch (block.type) {
        case "paragraph":
          return <p key={index} className="text-xs font-bold text-gray-700 mb-2">{block.content}</p>;
        case "list":
          return (
            <div key={index} className="mb-3">
              <h3 className="font-bold text-xs mb-1">{block.title}</h3>
              <ul className="list-disc list-inside ml-4 text-sm text-gray-700">
                {block.items.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </div>
          );
        case "heading":
          return <span key={index} className="text-lg font-bold mb-2">{block.content}</span>;
        case "item":
          return (
            <div key={index} className="mb-3 p-2 border border-gray-200 rounded-md bg-white shadow-sm">
              <h4 className="font-semibold text-sm text-xs text-blue-700">{block.name}</h4>
              <p className="text-xs text-gray-600">{block.description}</p>
              {block.recommendation && <p className="text-green-600 text-xs mt-1">Recommendation: {block.recommendation}</p>}
            </div>
          );
        case "booking":
          return (
            <div key={index} className="mb-3 p-2 border border-gray-200 rounded-md bg-white shadow-sm">
              <h4 className="font-bold text-sm">{block.service} Booking</h4>
              <p className="text-xs text-gray-600">{block.description}</p>
              <p className={`text-xs mt-1 ${block.status === "Confirmed" ? "text-green-600" : "text-yellow-600"}`}>
                Status: {block.status}
              </p>
              <p className="text-xs text-gray-500">Booking ID: {block.bookingId}</p>
            </div>
          );
        case "suggestion":
          return (
            <div key={index} className="mb-3 p-2 border border-gray-200 rounded-md bg-white shadow-sm">
              <h4 className="font-bold text-sm text-purple-700">{block.title}</h4>
              <p className="text-xs text-gray-600">{block.description}</p>
              <span className="inline-block bg-purple-100 text-purple-700 text-xs px-2 py-1 rounded-full mt-1">
                {block.category}
              </span>
            </div>
          );
        case "location":
          return (
            <div key={index} className="mb-3 p-2 border border-gray-200 rounded-md bg-white shadow-sm">
              <h4 className="font-bold text-sm text-red-700">{block.name}</h4>
              <p className="text-xs text-gray-600">{block.description}</p>
              <p className="text-xs text-gray-500 mt-1">Coordinates: {block.coordinates}</p>
            </div>
          );
        case "note":
          return (
            <div key={index} className="mb-3 p-2 border border-yellow-300 bg-yellow-50 rounded-md text-yellow-800 text-xs">
              <strong>Note:</strong> {block.content}
            </div>
          );
        case "dailyItinerary":
          const days = block.days;
          const selectedDay = days[selectedDayIndex];

          return (
            <div key={index} className="h-full w-full ">
              <div className="flex flex-wrap gap-2 mb-4">
                {days.map((day, dayIndex) => (
                  <button
                    key={dayIndex}
                    className={`px-4 py-2 rounded-full text-xs font-bold transition-colors duration-200 
                      ${selectedDayIndex === dayIndex
                        ? "bg-blue-600 text-white shadow-md"
                        : "bg-gray-200 text-gray-700 hover:bg-blue-100 hover:text-blue-700"
                      }`}
                    onClick={() => {
                      setSelectedDayIndex(dayIndex);
                      if (onDayClick) {
                        onDayClick(day.locations || []);
                      }
                    }}
                  >
                    {day.date}
                  </button>
                ))}
              </div>

              {selectedDay && (
                <div className=" p-4 border border-gray-200 rounded-lg shadow-lg bg-gray-50">
                  <h3 className="text-xs font-bold text-blue-700 mb-2 border-b pb-1 border-blue-100">{selectedDay.date}</h3>
                  <div className="relative pl-7">
                    {selectedDay.activities.map((activity, activityIndex) => (
                      <div key={activityIndex} className="flex items-start mb-4 relative">
                        <div className="w-20 text-right text-xs font-bold text-gray-800">
                          {activity.time}
                        </div>
                        <div className="absolute left-0 top-0 h-full w-0.5 bg-blue-200 rounded-full"></div>
                        <div className="absolute left-[-8px] top-0 w-4 h-4 rounded-full bg-blue-600 flex items-center justify-center text-white text-xxs font-bold z-10"></div>
                        <div className="ml-6 flex-1">
                          <p className="font-bold text-xs text-gray-900">{activity.description}</p>
                          {activity.details && <p className="text-xs text-gray-600 whitespace-pre-line mt-0.5">{activity.details}</p>}
                          {activity.action && (
                            <button className="mt-1.5 px-3 py-1.5 bg-blue-600 text-white rounded-full text-xs font-medium hover:bg-blue-700 transition-colors duration-200">
                              {activity.action}
                            </button>
                          )}
                          {activity.longDescription && <p className="text-xs text-gray-700 mt-1 leading-relaxed">{activity.longDescription}</p>}
                        </div>
                      </div>
                    ))}
                  </div>
                  {selectedDay.dailyCost && (
                    <div className="mt-4 p-3 bg-blue-100 rounded-md text-blue-800 text-xs">
                      <h4 className="font-bold">Daily Cost: {selectedDay.dailyCost.currency}{selectedDay.dailyCost.amount}</h4>
                      <p>{selectedDay.dailyCost.details}</p>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        case "packageSavings":
          return (
            <div key={index} className="mb-4 p-4 border border-green-400 bg-green-50 rounded-lg shadow-md">
              <h4 className="font-bold text-lg text-green-800 mb-1">{block.title}</h4>
              <p className="text-sm text-gray-700 mb-2">{block.description}</p>
              <div className="flex justify-between items-center text-sm text-gray-800">
                <span>Original Cost: <span className="line-through">{block.originalCost.currency}{block.originalCost.amount}</span></span>
                <span>Package Cost: <span className="font-bold">{block.packageCost.currency}{block.packageCost.amount}</span></span>
              </div>
              <p className="text-green-600 font-bold text-base mt-2">{block.message}</p>
            </div>
          );
        case "packageBooking":
          return (
            <div key={index} className="mb-3 p-3 border border-green-300 rounded-md bg-green-50 shadow-sm">
              <h4 className="font-bold text-sm text-green-700">{block.service} Booking</h4>
              <p className="text-xs text-gray-600">{block.description}</p>
              <p className={`text-xs mt-1 ${block.status === "Confirmed" ? "text-green-600" : "text-yellow-600"}`}>
                Status: {block.status}
              </p>
              <p className="text-xs text-gray-500">Booking ID: {block.bookingId}</p>
              {block.savings && (
                <p className="text-green-600 font-bold text-xs mt-1">Savings: {block.savings.currency}{block.savings.amount}</p>
              )}
              {block.message && <p className="text-green-600 text-xs mt-1">{block.message}</p>}
            </div>
          );
        default:
          return null;
      }
    });
  };

  return (
    <>
      <div className="flex h-full w-full bg-gray-100 p-4 rounded-lg shadow-inner">
        {/* Left Section - Map */}
        <div className="w-[35%] p-3 mr-4 bg-white rounded-lg shadow-md flex items-center justify-center overflow-hidden">
          {MapComponent}
        </div>

        <div className="flex flex-col w-[65%] bg-gray-50 px-5 pt-2 rounded-lg shadow-lg">

          <div className=" flex-col md:flex-row justify-between items-start md:items-center  pb-3 border-b border-gray-200">
            <h1 className="flex text-2xl font-extrabold text-gray-900 mb-1 md:mb-0">{planData?.city}</h1>
            <div className="flex items-center text-gray-600 text-base">
              <span className="mr-3 text-xs font-bold">{planData?.dates}</span>
              <span className="flex text-xs items-center text-sm">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clipRule="evenodd" />
                </svg>
                {planData?.locations}
              </span>
            </div>
          </div>

          <div className="mb-2 p-3 bg-blue-50 border border-blue-200 rounded-md shadow-sm">
            <p className="text-blue-800 italic text-xs">{planData?.notes}</p>
          </div>

          <div className="mb-2 p-4 bg-white rounded-md shadow-md h-[15%] overflow-y-auto">
            {/* <h2 className="text-xl font-bold text-gray-800 mb-2">{planData?.tripDescription?.title}</h2> */}
            <p className="text-sm text-gray-700 text-xs leading-relaxed">{planData?.tripDescription?.content}</p>
          </div>

          <div className="flex flex-wrap border-b border-gray-300 mb-2">
            {(filteredTabs || planData?.tabs).map((tab, index) => (
              <button
                key={index}
                className={`px-3 py-2 text-xs font-bold transition-all duration-200 ease-in-out 
                  ${activeTab === tab
                    ? "text-blue-600 border-b-3 border-blue-600 bg-blue-50"
                    : "text-gray-700 hover:text-blue-500 hover:border-b-3 hover:border-blue-300"
                  } focus:outline-none`}
                onClick={() => setActiveTab(tab)}
              >
                {tab}
              </button>
            ))}
          </div>

          {/* Dynamic Tab Content */}
          <div className="flex-grow overflow-y-auto p-3 bg-white rounded-md shadow-md mb-4 h-[60%]">
            {renderTabContent()}
          </div>
        </div>
      </div>
    </>
  );
}

export default DisplayPlan;
