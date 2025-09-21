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

const sampleSpots = [
  { latitude: 28.6139, longitude: 77.2090, name: "India Gate" },
  { latitude: 28.5245, longitude: 77.1855, name: "Qutub Minar" },
  { latitude: 28.6562, longitude: 77.2410, name: "Red Fort" }
];

const sampleOrigin = "New Delhi, India";
const sampleDestination = "Agra, India";
const sampleWaypoints = [
  { location: "Mathura, India", stopover: true },
  { location: "Vrindavan, India", stopover: true }
];


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/plan" element={<Planner />} />
        <Route path="/plan/form" element={<PlanForm />} />
        <Route path="/plan/prompt" element={<PlanPrompt />} />
        <Route path="/plan/result/:planId" element={<PlanResult />} />
        <Route path="/trip-overview/:tripId" element={<TripOverview />} />
        <Route path="/paymentgateway" element={<PaymentGateway />} />
        <Route path="*" element={<Loading />} />
        <Route path="/map" element={
          <div>
            <h1>My Spots Map</h1>
            <MapLoader>
              <MapComponentWrapper />
            </MapLoader>
          </div>
        } />
        <Route path="/umap" element={
          <MapLoader>
            <MapView
              spots={sampleSpots}
              origin={sampleOrigin}
              destination={sampleDestination}
              waypoints={sampleWaypoints}
            />
          </MapLoader>
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
      { "name": "India Gate", "latitude": 28.6129, "longitude": 77.2295 },
      { "name": "Qutub Minar", "latitude": 28.5245, "longitude": 77.1855 },
      { "name": "Red Fort", "latitude": 28.6562, "longitude": 77.2410 },
      { "name": "Humayun's Tomb", "latitude": 28.5933, "longitude": 77.2507 },
      { "name": "Lotus Temple", "latitude": 28.5535, "longitude": 77.2588 },
    ];
    setSpots(sampleSpots);

    if (sampleSpots.length > 0) {
      setOrigin(sampleSpots[0].name);
      setDestination(sampleSpots[sampleSpots.length - 1].name);
      setWaypoints(
        sampleSpots.slice(1, sampleSpots.length - 1).map(spot => ({
          location: spot.name,
          stopover: true
        }))
      );
    }
  }, []);

  return <MapView spots={spots} origin={origin} destination={destination} waypoints={waypoints} />;
};

export default App;
