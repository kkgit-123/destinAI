import React from 'react';
import { LoadScript } from '@react-google-maps/api';

const libraries = ["places", "geometry", "drawing", "visualization"]; // Add any necessary libraries

const MapLoader = ({ children }) => {
  const apiKey = process.env.REACT_APP_GOOGLE_MAPS_API_KEY;

  return (
    <LoadScript
      googleMapsApiKey={apiKey}
      loadingElement={<div>Loading Maps...</div>}
      libraries={libraries}
    >
      {children}
    </LoadScript>
  );
};

export default MapLoader;
