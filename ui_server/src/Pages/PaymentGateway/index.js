import React from 'react';
import ThemedHeader from '../../components/ThemedHeader';
import Breadcrumbs from '../../components/Breadcrumbs';

function PaymentGateway() {
  return (
    <div className='w-screen h-screen flex flex-col'>
      <div className='flex w-screen h-[10%] mb-1'>
        <ThemedHeader>
          <div className="flex items-center">
            <img src="/logo.svg" alt="EaseMyTrip" className="h-[2.5%] mr-4" />
            <span className="font-bold text-lg text-gray-800">Payment Gateway</span>
          </div>
          <div className="flex items-center space-x-4">
           
          </div>
        </ThemedHeader>
      </div>
      <div className="bg-white shadow-md w-full h-[5%] flex items-center justify-center">
        <Breadcrumbs currentStep={5} /> {/* Assuming this is step 5 in a flow */}
      </div>

      <div className="flex-grow flex items-center justify-center bg-gray-100 p-6">
        <div className="bg-white p-8 rounded-xl shadow-lg border border-gray-200 text-center max-w-md w-full">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Secure Payment</h2>
          <p className="text-gray-600 mb-6">This is a dummy payment gateway page.</p>
          <div className="space-y-4">
            <input
              type="text"
              placeholder="Card Number"
              className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              type="text"
              placeholder="Card Holder Name"
              className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <div className="flex space-x-4">
              <input
                type="text"
                placeholder="MM/YY"
                className="w-1/2 p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <input
                type="text"
                placeholder="CVV"
                className="w-1/2 p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <button className="w-full bg-green-600 text-white py-3 rounded-md hover:bg-green-700 font-semibold transition duration-300">
              Pay Now
            </button>
          </div>
          <p className="text-gray-500 text-xs mt-6">Your payment is secured by industry-standard encryption.</p>
        </div>
      </div>
    </div>
  );
}

export default PaymentGateway;
