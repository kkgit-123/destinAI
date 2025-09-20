import React from 'react';

function BookingConfirmationBanner({ confirmedMessage, referenceNo, emailMessage }) {
  return (
    <div className="bg-blue-100 p-4 rounded-lg flex items-center justify-between shadow-sm mb-6">
      <div className="flex items-center">
        <span className="text-2xl mr-3">🎉</span> {/* Confetti emoji */}
        <div>
          <p className="text-blue-800 font-semibold text-sm">{confirmedMessage}</p>
          <p className="text-blue-600 text-xs">Reference No: {referenceNo} • {emailMessage}</p>
        </div>
      </div>
      <span className="text-blue-400 text-2xl">✈️</span> {/* Paper plane emoji */}
    </div>
  );
}

export default BookingConfirmationBanner;
