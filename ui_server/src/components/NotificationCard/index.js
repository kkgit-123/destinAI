import React from 'react';

function NotificationCard({ icon, message, date }) {
  return (
    <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl mb-4">
      <h3 className="text-lg font-bold text-gray-800 mb-3 border-b pb-2">Notifications & Alerts</h3>
      <div className="flex items-center space-x-3">
        <span className="text-blue-500 text-xl">{icon}</span>
        <div>
          <p className="text-gray-700 text-sm">{message}</p>
          <p className="text-gray-500 text-xs">{date}</p>
        </div>
      </div>
    </div>
  );
}

export default NotificationCard;
