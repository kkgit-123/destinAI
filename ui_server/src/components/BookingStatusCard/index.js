import React from 'react';
import { useNavigate } from 'react-router-dom';

function BookingStatusCard({ bookings }) {
  const navigate = useNavigate();

  const getStatusColor = (status) => {
    switch (status.toLowerCase()) {
      case 'confirmed':
        return 'text-green-600';
      case 'pending':
        return 'text-yellow-600';
      case 'in progress':
        return 'text-blue-600';
      case 'cancelled':
        return 'text-red-600';
      default:
        return 'text-gray-600';
    }
  };

  const handlePaymentClick = () => {
    navigate('/paymentgateway');
  };

  return (
    <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl mb-4">
      <h3 className="text-lg font-bold text-gray-800 mb-3 border-b pb-2">Booking Status</h3>
      <div className="space-y-3">
        {bookings.map((booking, index) => (
          <div key={index} className="flex justify-between items-center">
            <div>
              <p className="text-gray-700 text-sm font-semibold">{booking.service}</p>
              <p className="text-gray-500 text-xs">{booking.details}</p>
            </div>
            <div className="flex items-center space-x-2">
              <span className={`text-sm font-bold ${getStatusColor(booking.status)}`}>
                {booking.status}
              </span>
              {booking.status.toLowerCase() === 'pending' && (
                <button
                  onClick={handlePaymentClick}
                  className="bg-blue-500 hover:bg-blue-600 text-white text-xs px-3 py-1 rounded-md transition duration-300"
                >
                  Pay Now
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default BookingStatusCard;
