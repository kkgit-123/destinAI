import React, { useState, useEffect, useMemo } from 'react';
import { GoogleMap, Marker, DirectionsRenderer, DirectionsService } from '@react-google-maps/api';

const containerStyle = {
  width: '100%',
  height: '100%'
};

const MapView = ({ spots }) => { // Removed origin, destination, waypoints for debugging
  // const [response, setResponse] = useState(null); // Removed for debugging

  console.log("MapView received spots:", spots); // Debugging line

  const mapCenter = useMemo(() => {
    if (spots && spots.length > 0) {
      const totalLat = spots.reduce((sum, spot) => sum + spot.latitude, 0);
      const totalLng = spots.reduce((sum, spot) => sum + spot.longitude, 0);
      return {
        lat: totalLat / spots.length,
        lng: totalLng / spots.length,
      };
    }
    return {
      lat: 28.6139,   // Default to New Delhi if no spots
      lng: 77.2090
    };
  }, [spots]);

  // Removed directionsServiceOptions and directionsCallback for debugging

  return (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={mapCenter}
      zoom={spots && spots.length > 0 ? 10 : 8} // Zoom in if there are spots
    >
      {spots && spots.map((spot, index) => (
        <Marker
          key={index}
          position={{ lat: spot.latitude, lng: spot.longitude }}
          title={spot.name}
        />
      ))}

      {/* Removed DirectionsService and DirectionsRenderer for debugging */}
    </GoogleMap>
  );
};

export default MapView;
