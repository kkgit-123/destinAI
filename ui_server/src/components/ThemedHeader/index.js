import React from 'react';

function ThemedHeader({ children }) {
  return (
    <header className="flex h-[100%] w-[100%] bg-white shadow-md">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        {children}
      </div>
    </header>
  );
}

export default ThemedHeader;
