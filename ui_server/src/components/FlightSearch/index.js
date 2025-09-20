import React from 'react';

function FlightSearch() {
  return (
    <div className="  flex h-[100%] w-[100%] bg-gradient-to-r from-[#3081ED] to-[#55C9F1] py-8 md:py-12 lg:py-16">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center mb-6">
          <div className="flex space-x-2 md:space-x-4 mb-4 md:mb-0">
            <button className="bg-white text-blue-600 px-4 py-2 md:px-6 md:py-2 rounded-full font-semibold text-sm md:text-base">One Way</button>
            <button className="text-white px-4 py-2 md:px-6 md:py-2 rounded-full hover:bg-blue-600 text-sm md:text-base">Round Trip</button>
            <button className="text-white px-4 py-2 md:px-6 md:py-2 rounded-full hover:bg-blue-600 text-sm md:text-base">Multicity</button>
          </div>
          <h2 className="text-white text-xl md:text-2xl font-bold">Search Lowest Price</h2>
        </div>

        <div className="bg-white rounded-lg shadow-lg p-4 md:p-6 grid grid-cols-1 md:grid-cols-5 gap-4 items-end">
          <div className="col-span-1">
            <label className="block text-gray-600 text-xs md:text-sm font-semibold mb-1">FROM</label>
            <input type="text" placeholder="Delhi" className="w-full p-2 border border-gray-300 rounded-md text-base md:text-lg font-bold" />
            <p className="text-xs md:text-sm text-gray-500 mt-1">[DEL] Indira Gandhi International Airport</p>
          </div>
          <div className="col-span-1">
            <label className="block text-gray-600 text-xs md:text-sm font-semibold mb-1">TO</label>
            <input type="text" placeholder="Mumbai" className="w-full p-2 border border-gray-300 rounded-md text-base md:text-lg font-bold" />
            <p className="text-xs md:text-sm text-gray-500 mt-1">[BOM] Chhatrapati Shivaji International A...</p>
          </div>
          <div className="col-span-1">
            <label className="block text-gray-600 text-xs md:text-sm font-semibold mb-1">DEPARTURE DATE</label>
            <input type="text" value="15 Sep 2025" className="w-full p-2 border border-gray-300 rounded-md text-base md:text-lg font-bold" />
            <p className="text-xs md:text-sm text-gray-500 mt-1">Monday</p>
          </div>
          <div className="col-span-1">
            <label className="block text-gray-600 text-xs md:text-sm font-semibold mb-1">RETURN DATE</label>
            <input type="text" placeholder="Book a round trip to save more" className="w-full p-2 border border-gray-300 rounded-md text-xs md:text-sm" />
          </div>
          <button className="col-span-1 bg-orange-500 text-white px-6 py-3 md:px-8 md:py-4 rounded-md text-lg md:text-xl font-bold hover:bg-orange-600">
            SEARCH
          </button>
        </div>

        <div className="flex flex-col md:flex-row items-center justify-between mt-6 text-white text-sm md:text-base">
          <div className="flex flex-wrap justify-center md:justify-start items-center space-x-2 md:space-x-4 mb-4 md:mb-0">
            <span className="font-semibold">Special Fares (Optional):</span>
            <label className="inline-flex items-center">
              <input type="radio" className="form-radio text-blue-600" name="specialFares" />
              <span className="ml-2">Defence Forces</span>
            </label>
            <label className="inline-flex items-center">
              <input type="radio" className="form-radio text-blue-600" name="specialFares" />
              <span className="ml-2">Students</span>
            </label>
            <label className="inline-flex items-center">
              <input type="radio" className="form-radio text-blue-600" name="specialFares" />
              <span className="ml-2">Senior Citizens</span>
            </label>
            <label className="inline-flex items-center">
              <input type="radio" className="form-radio text-blue-600" name="specialFares" />
              <span className="ml-2">Doctors Nurses</span>
            </label>
          </div>
          <div className="flex items-center">
            <input type="checkbox" className="form-checkbox text-blue-600" id="bookHotel" />
            <label htmlFor="bookHotel" className="ml-2">Book Hotel & Get up to 45% OFF*</label>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FlightSearch;
