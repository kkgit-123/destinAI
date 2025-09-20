import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import './App.css'; 
import { lazy } from "react";
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
        
      </Routes>
    </Router>
  );
}

export default App;
