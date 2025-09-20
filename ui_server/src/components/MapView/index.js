import React, { useState, useEffect } from 'react';
import { GoogleMap, Marker, DirectionsRenderer, DirectionsService } from '@react-google-maps/api';

const containerStyle = {
  width: '100%',
  height: '400px'
};

const defaultCenter = {
  lat: 28.6139,   // example: New Delhi
  lng: 77.2090
};

const MapView = ({ spots, origin, destination, waypoints }) => {
  const [response, setResponse] = useState(null);
  const directionsServiceOptions = {
    destination: destination,
    origin: origin,
    waypoints: waypoints,
    travelMode: 'DRIVING'
  };

  const directionsCallback = (res) => {
    if (res !== null) {
      if (res.status === 'OK') {
        setResponse(res);
      } else {
        console.log('response: ', res);
      }
    }
  };

  return (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={defaultCenter}
      zoom={8}
    >
      {spots && spots.map((spot, index) => (
        <Marker
          key={index}
          position={{ lat: spot.latitude, lng: spot.longitude }}
          title={spot.name}
        />
      ))}

      {origin && destination && (
        <DirectionsService
          options={directionsServiceOptions}
          callback={directionsCallback}
        />
      )}

      {response !== null && (
        <DirectionsRenderer
          options={{
            directions: response
          }}
        />
      )}
    </GoogleMap>
  );
};

export default MapView;
