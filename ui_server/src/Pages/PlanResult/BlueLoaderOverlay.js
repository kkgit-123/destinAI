import React from 'react';
import Lottie from 'lottie-react';
import blueLoadingAnimation from '../../animations/blue loading.json';

const BlueLoaderOverlay = () => {
  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-white bg-opacity-80 backdrop-blur-md">
      <div className="flex flex-col items-center justify-center text-center text-gray-800 text-2xl font-bold">
        <Lottie animationData={blueLoadingAnimation} loop={true} style={{ width: 150, height: 150 }} />
      </div>
    </div>
  );
};

export default BlueLoaderOverlay;
