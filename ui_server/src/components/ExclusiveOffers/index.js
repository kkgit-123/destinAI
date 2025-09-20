import React from 'react';

function ExclusiveOffers (){
  return (
    <div className=" flex h-[100%] w-[100%] bg-gray-100 py-8 md:py-12">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-8">Exclusive Offers</h2>

        <div className="flex justify-center space-x-2 md:space-x-4 mb-8">
          <button className="bg-blue-600 text-white px-4 py-2 rounded-md text-sm md:text-base">Best Offers</button>
          <button className="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-md text-sm md:text-base">Bank Offers</button>
          <button className="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-md text-sm md:text-base">Flight</button>
          <button className="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-md text-sm md:text-base">Hotel</button>
          <button className="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-md text-sm md:text-base">Bus</button>
          <button className="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-md text-sm md:text-base">Holidays</button>
          <button className="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-md text-sm md:text-base">Cabs</button>
          <a href="#" className="text-blue-600 hover:underline px-4 py-2 text-sm md:text-base">View All Offers</a>
        </div>

        <div className="flex overflow-x-auto space-x-4 pb-4">
          {/* Offer Card 1 */}
          <div className="flex-shrink-0 w-[25%] md:w-[30%] bg-white rounded-lg shadow-lg p-4">
            <div className="relative h-[15%] mb-4">
              <img src="https://via.placeholder.com/300x150" alt="Offer" className="w-full h-full object-cover rounded-md" />
              <div className="absolute top-2 left-2 bg-blue-500 text-white text-xs px-2 py-1 rounded-full">New User Offer on</div>
              <div className="absolute bottom-2 left-2 text-white text-xl font-bold">First Flight</div>
            </div>
            <h3 className="text-lg font-semibold mb-2">Register and Get Discount on Booking First Flight with Us</h3>
            <p className="text-sm text-gray-600">Valid till: 30th Sep, 2025</p>
            <div className="mt-4 bg-gray-200 text-gray-800 px-3 py-1 rounded-md text-sm flex items-center justify-between">
              <span>Use Code: <span className="font-bold">EMTFIRST</span></span>
              <button>📋</button>
            </div>
          </div>

          {/* Offer Card 2 */}
          <div className="flex-shrink-0 w-[25%] md:w-[30%] bg-white rounded-lg shadow-lg p-4">
            <div className="relative h-[15%] mb-4">
              <img src="https://via.placeholder.com/300x150" alt="Offer" className="w-full h-full object-cover rounded-md" />
              <div className="absolute top-2 left-2 bg-purple-500 text-white text-xs px-2 py-1 rounded-full">Grand Runaway Fest by</div>
              <div className="absolute bottom-2 left-2 text-white text-xl font-bold">IndiGo Airlines</div>
            </div>
            <h3 className="text-lg font-semibold mb-2">Book Flights with IndiGo Airlines at Fares Starting From INR 1,299*</h3>
            <p className="text-sm text-gray-600">Valid till: 21st Sep, 2025</p>
            <div className="mt-4 bg-gray-200 text-gray-800 px-3 py-1 rounded-md text-sm flex items-center justify-between">
              <span>Use Code: <span className="font-bold">INDIGO</span></span>
              <button>📋</button>
            </div>
          </div>

          {/* Offer Card 3 */}
          <div className="flex-shrink-0 w-[25%] md:w-[30%] bg-white rounded-lg shadow-lg p-4">
            <div className="relative h-[15%] mb-4">
              <img src="https://via.placeholder.com/300x150" alt="Offer" className="w-full h-full object-cover rounded-md" />
              <div className="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded-full">Exclusive Deals on</div>
              <div className="absolute bottom-2 left-2 text-white text-xl font-bold">Malaysia Airlines</div>
            </div>
            <h3 className="text-lg font-semibold mb-2">Enjoy Up to INR 1,500 OFF* & Extra Baggage Allowance on Flights with Malaysia Airlines</h3>
            <p className="text-sm text-gray-600">Valid till: 30th Sep, 2025</p>
            <div className="mt-4 bg-gray-200 text-gray-800 px-3 py-1 rounded-md text-sm flex items-center justify-between">
              <span>Use Code: <span className="font-bold">EMTMA</span></span>
              <button>📋</button>
            </div>
          </div>

          {/* Offer Card 4 */}
          <div className="flex-shrink-0 w-[25%] md:w-[30%] bg-white rounded-lg shadow-lg p-4">
            <div className="relative h-[15%] mb-4">
              <img src="https://via.placeholder.com/300x150" alt="Offer" className="w-full h-full object-cover rounded-md" />
              <div className="absolute top-2 left-2 bg-green-500 text-white text-xs px-2 py-1 rounded-full">Fly to Kuala Lumpur with</div>
              <div className="absolute bottom-2 left-2 text-white text-xl font-bold">Malaysia Airlines</div>
            </div>
            <h3 className="text-lg font-semibold mb-2">Book Flights to Thiruvananthapuram, Kuala Lumpur at Fares Starting From INR 1,299*</h3>
            <p className="text-sm text-gray-600">Valid till: 30th Sep, 2025</p>
            <div className="mt-4 bg-gray-200 text-gray-800 px-3 py-1 rounded-md text-sm flex items-center justify-between">
              <span>Use Code: <span className="font-bold">EMTKUL</span></span>
              <button>📋</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExclusiveOffers;
