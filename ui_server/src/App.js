import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import './App.css'; 
import { lazy } from "react";
import Loading from './Pages/Loading';
import MapLoader from './components/MapLoader';
import MapView from './components/MapView';
const Planner = lazy(() => import("./Pages/Planner"));
const PlanForm = lazy(() => import("./Pages/PlanForm"));
const PlanPrompt = lazy(() => import("./Pages/PlanPrompt"));
const PlanResult = lazy(() => import("./Pages/PlanResult"));
const TripOverview = lazy(() => import("./Pages/TripOverview"));
const PaymentGateway = lazy(() => import("./Pages/PaymentGateway"));
// AIzaSyCPoPxzYWl9sh_0P7Giwsl2ph4xx8cLGMs
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/plan" element={<Planner/>} />
        <Route path="/plan/form" element={<PlanForm/>} />
        <Route path="/plan/prompt" element={<PlanPrompt/>} />
        <Route path="/plan/result/:planId" element={<PlanResult/>} />
        <Route path="/trip-overview/:tripId" element={<TripOverview/>} />
         <Route path="/paymentgateway" element={<PaymentGateway/>} />
         <Route path="*" element={<Loading/>} />
         <Route path="/map" element={
            <div>
              <h1>My Spots Map</h1>
              <MapLoader>
                <MapComponentWrapper />
              </MapLoader>
            </div>
         } />
      </Routes>
    </Router>
  );
}

const MapComponentWrapper = () => {
  const [spots, setSpots] = useState([]);
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');
  const [waypoints, setWaypoints] = useState([]);

  useEffect(() => {
    const sampleSpots = [
      {"name": "India Gate", "latitude": 28.6129, "longitude": 77.2295},
      {"name": "Qutub Minar", "latitude": 28.5245, "longitude": 77.1855},
      {"name": "Red Fort", "latitude": 28.6562, "longitude": 77.2410},
      {"name": "Humayun's Tomb", "latitude": 28.5933, "longitude": 77.2507},
      {"name": "Lotus Temple", "latitude": 28.5535, "longitude": 77.2588},
    ];
    setSpots(sampleSpots);

    if (sampleSpots.length > 0) {
      setOrigin({ lat: sampleSpots[0].latitude, lng: sampleSpots[0].longitude });
      setDestination({ lat: sampleSpots[sampleSpots.length - 1].latitude, lng: sampleSpots[sampleSpots.length - 1].longitude });
      setWaypoints(
        sampleSpots.slice(1, sampleSpots.length - 1).map(spot => ({
          location: { lat: spot.latitude, lng: spot.longitude },
          stopover: true
        }))
      );
    }
  }, []);

  return <MapView spots={spots} origin={origin} destination={destination} waypoints={waypoints} />;
};

export default App;
