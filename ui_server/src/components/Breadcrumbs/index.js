import React from 'react';
import { useNavigate } from 'react-router-dom';
import { FaCheck } from 'react-icons/fa'; // Assuming react-icons is available, otherwise use a simple SVG

const Breadcrumbs = ({ currentStep }) => {
  const navigate = useNavigate();
  const steps = ['Choose Mode', 'Trip Details', 'Itinerary', 'Booking & Conformation'];
  const routes = ['/plan', '/plan/form', '/plan/result/1', '/trip-overview/1']; // Updated routes to match App.js

  const handleStepClick = (index) => {
    if (index <= currentStep) {
      navigate(routes[index]);
    }
  };

  return (
    <div className="flex pl-10 items-center justify-center w-[45%] py-2">
      {steps.map((step, index) => (
        <React.Fragment key={step}>
          <div
            className={`flex items-center ${index <= currentStep ? 'cursor-pointer' : 'cursor-not-allowed'}`}
            onClick={() => handleStepClick(index)}
          >
            <button
              className={`w-4 h-4 rounded-full flex items-center justify-center text-white font-bold text-xs
                ${index < currentStep ? 'bg-green-500' : index === currentStep ? 'bg-blue-500' : 'bg-gray-400'}`}
              disabled={index > currentStep}
            >
              {index < currentStep ? <FaCheck size={8} /> : index + 1}
            </button>
            <span className={`text-xs ml-1 ${index < currentStep ? 'text-green-600' : index === currentStep ? 'text-blue-600' : 'text-gray-500'}`}>
              {step}
            </span>
          </div>
          {index < steps.length - 1 && (
            <div
              className={`flex-grow h-0.5 mx-1 ${index < currentStep ? 'bg-green-500' : 'bg-gray-400'}`}
              style={{ width: '5%' }}
            ></div>
          )}
        </React.Fragment>
      ))}
    </div>
  );
};

export default Breadcrumbs;
