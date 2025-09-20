import React from 'react';

function Header () {
    
  return (
    <header className=" flex h-[100%] w-[100%] bg-white shadow-md">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center">
          <img src="/logo.svg" alt="EaseMyTrip" className="h-[2.5%] mr-4" /> {/* Placeholder for logo */}
          <nav className="hidden md:flex space-x-6">
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">✈️</span> Flights
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🏨</span> Hotels
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">✈️🏨</span> Flight+Hotel
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🚆</span> Trains
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🚌</span> Bus
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🏖️</span> Holidays
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🚕</span> Cabs
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🗺️</span> Activities
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">🛂</span> Visa
            </a>
            <a href="#" className="text-gray-700 hover:text-blue-600 flex items-center">
              <span className="mr-1">•••</span> More
            </a>
          </nav>
        </div>

        <div className="flex items-center space-x-4">
          <div className="hidden md:flex items-center text-gray-700">
            <span>Customer Service </span>
            <svg className="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
          </div>
          <div className="flex items-center text-gray-700">
            <img src="https://flagcdn.com/in.svg" alt="India" className="h-[1.25%] w-[1.25%] mr-1" />
            <span>India </span>
            <svg className="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
          </div>
          <div className="text-gray-700">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 3v1m0 16v1m9-9h1M3 12H2m15.325-4.243l.707-.707M3.929 19.071l.707-.707m0-10.607l-.707-.707M19.071 3.929l-.707.707M18.364 18.364l.707.707M4.929 4.929l-.707-.707"></path></svg>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
