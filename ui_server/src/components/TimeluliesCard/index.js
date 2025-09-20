import React from 'react';

function TimeluliesCard({ title, items }) {
  return (
    <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl mb-4">
      <h3 className="text-lg font-bold text-gray-800 mb-3 border-b pb-2">{title}</h3>
      <div className="space-y-2">
        {items.map((item, index) => (
          <div key={index} className="flex items-center justify-between">
            <p className="text-gray-700 text-sm">{item.name}</p>
            <span className="text-gray-500 text-xs">{item.time}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TimeluliesCard;
