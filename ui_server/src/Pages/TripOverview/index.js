import React, { useEffect, useState, useMemo } from 'react';
import { useParams } from 'react-router-dom'; // Import useParams
import planData from '../../constants/planData'; // Import planData as fallback
import { ENDPOINTS } from '../../constants/endpoints';
import ThemedHeader from '../../components/ThemedHeader';
import Breadcrumbs from '../../components/Breadcrumbs';
import BookingConfirmationBanner from '../../components/BookingConfirmationBanner';
import ItineraryCard from '../../components/ItineraryCard';
import NotificationCard from '../../components/NotificationCard';
import BookingStatusCard from '../../components/BookingStatusCard';
import MapView from "../../components/MapView"; // Import MapView
import { useLoadScript } from '@react-google-maps/api'; // Import useLoadScript
import logo from "../../Images/favicon.ico"
function TripOverview() {
    const { tripId } = useParams(); // Get tripId from URL parameters
    const [currentPlanData, setCurrentPlanData] = useState(null); // Initialize with null, will be set by fetch
    const [selectedLocations, setSelectedLocations] = useState([]); // State to hold locations for the selected day

    const { isLoaded, loadError } = useLoadScript({
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
        libraries: ["places"], // Add any necessary libraries
    });

    useEffect(() => {
        const fetchPlanData = async () => {
            let dataToUse = planData; // Default to local fallback

            if (tripId) {
                try {
                    const response = await fetch(`${ENDPOINTS.PLAN_DATA}/${tripId}`);
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    dataToUse = await response.json();
                } catch (error) {
                    console.error("Failed to fetch plan data:", error);
                    alert("Failed to load plan data from server. Using local data.");
                }
            } else {
                console.warn("No tripId found, using local data.");
            }
            
            setCurrentPlanData(dataToUse);
            console.log("Current Plan Data after fetch/fallback:", dataToUse); // Debugging line

            // Set initial locations from the first day if available in the dataToUse
            if (dataToUse && dataToUse.tabContent && dataToUse.tabContent.Itinerary && dataToUse.tabContent.Itinerary.length > 0 && dataToUse.tabContent.Itinerary[0].days && dataToUse.tabContent.Itinerary[0].days.length > 0) {
                setSelectedLocations(dataToUse.tabContent.Itinerary[0].days[0].locations || []);
            } else {
                setSelectedLocations([]); // Ensure it's an empty array if no locations are found
            }
        };
        fetchPlanData();
    }, [tripId]); // Add tripId to dependency array

    const MapComponent = useMemo(() => {
        if (loadError) return <div>Error loading maps</div>;
        if (!isLoaded) return <div>Loading Maps...</div>;
        console.log(selectedLocations)
        return <MapView spots={selectedLocations} />;
    }, [isLoaded, loadError, selectedLocations]);

    if (!currentPlanData) {
        return (
            <div className="flex items-center justify-center w-screen h-screen text-gray-500">
                Loading trip data...
            </div>
        );
    }

    const departure = currentPlanData.tabContent.Overview.find(item => item.type === 'departure');
    const weatherForecast = currentPlanData.tabContent.Weather.filter(item => item.type === 'weather');
    const packingChecklist = currentPlanData.tabContent.Packing.filter(item => item.type === 'item');
    const documents = currentPlanData.tabContent.Documents.filter(item => item.type === 'document');
    const budgetTracker = currentPlanData.tabContent.Budget.find(item => item.type === 'budget');
    const bookingConfirmation = currentPlanData.tabContent.Bookings.find(item => item.type === 'bookingConfirmation');
    const allBookings = currentPlanData.tabContent.Bookings.filter(item => item.type === 'booking' || item.type === 'packageBooking');
    const itineraryDays = currentPlanData.tabContent.Itinerary.find(item => item.type === 'dailyItinerary')?.days || [];

    const handleDayClick = (locations) => {
        console.log("handleDayClick called with locations:", locations); // Debugging line
        setSelectedLocations(locations);
    };

    const notificationData = {
        icon: "✈️",
        message: "Flight JL456 delayed by minutes.",
        date: "Nov 22, expect crowds."
    };

    return (
        <div className='w-screen h-screen flex flex-col'>
            <div className='flex w-screen h-[10%] mb-1'>
                <ThemedHeader>
                <div className="flex items-center">
                    {/* <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                    </svg> */}


<img src={logo} className="flex h-full w-auto object-contain">
                    </img>



                    <span className="font-bold text-lg text-gray-800">DestiniAI</span>
                </div>
                    
                </ThemedHeader>
            </div>
            <div className="bg-white shadow-md w-full h-[5%] flex items-center justify-center">
                <Breadcrumbs currentStep={4} />
            </div>

            <div className="h-[93%] bg-gray-100 text-xs p-6 font-sans overflow-auto">
                {bookingConfirmation && (
                    <BookingConfirmationBanner
                        confirmedMessage={bookingConfirmation.confirmedMessage}
                        referenceNo={bookingConfirmation.referenceNo}
                        emailMessage={bookingConfirmation.emailMessage}
                    />
                )}

                {/* Main content grid */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
                    {/* Left Column */}
                    <div className="md:col-span-2 grid grid-cols-1 gap-2">
                        {/* Top Row: Map and Days to Departure */}
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 flex flex-col transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                                <div className="w-full h-[70%] rounded-lg mb-3 shadow-sm">
                                    {MapComponent}
                                </div>
                                <p className="text-sm text-gray-500 text-center">Your personalized trip route</p>
                            </div>
                            <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 flex flex-col justify-center items-center text-center transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                                {departure && (
                                    <>
                                        <p className="text-lg font-extrabold text-gray-900 mb-2">{departure.days}</p>
                                        <p className="text-sm font-semibold text-gray-700 uppercase tracking-wide">Days to Departure</p>
                                        <p className="text-lg text-gray-500 mt-1">{departure.time}</p>
                                    </>
                                )}
                            </div>
                        </div>

                        {/* Itinerary Card */}
                        {itineraryDays.length > 0 && (
                            <ItineraryCard allDays={itineraryDays} onDayClick={handleDayClick} />
                        )}

                        {/* Documents */}
                        <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                            <h3 className="text-lg font-bold text-gray-800 mb-2 border-b pb-2">Documents</h3>
                            <div className="space-y-2">
                                {documents.map((doc, index) => (
                                    <p key={index} className="text-blue-700 flex items-center">
                                        <span className="mr-2 text-green-500">{doc.icon}</span>{doc.name}
                                    </p>
                                ))}
                            </div>
                        </div>
                    </div>

                    {/* Right Column */}
                    <div className="grid grid-cols-1 gap-2">
                        {/* Weather Forecast */}
                        <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                            <h3 className="text-lg font-bold text-gray-800 mb-4 border-b pb-2">Weather Forecast</h3>
                            <div className="flex justify-around items-center space-x-4">
                                {weatherForecast.map((weather, index) => (
                                    <div key={index} className="text-center flex flex-col items-center">
                                        <p className="text-4xl mb-1">{weather.icon}</p>
                                        <p className="font-semibold text-gray-700">{weather.city}</p>
                                        <p className="text-sm text-gray-500">{weather.temperature}</p>
                                    </div>
                                ))}
                            </div>
                        </div>

                        {/* Packing Checklist */}
                        <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                            <h3 className="text-lg font-bold text-gray-800 mb-3 border-b pb-2">Packing Checklist</h3>
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-y-2">
                                {packingChecklist.map((item, index) => (
                                    <label key={index} className="flex items-center text-gray-700 cursor-pointer">
                                        <input type="checkbox" className="mr-2 h-4 w-4 text-blue-600 rounded focus:ring-blue-500" defaultChecked={item.checked==="true"} />
                                        <span>{item.name}</span>
                                    </label>
                                ))}
                            </div>
                        </div>

                        {/* Booking Status */}
                        {allBookings.length > 0 && (
                            <BookingStatusCard bookings={allBookings} />
                        )}

                        {/* Notifications & Alerts */}
                        <NotificationCard
                            icon={notificationData.icon}
                            message={notificationData.message}
                            date={notificationData.date}
                        />

                        {/* Budget Tracker */}
                        <div className="bg-white p-5 rounded-xl shadow-md border border-gray-200 transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                            <h3 className="text-lg font-bold text-gray-800 mb-3 border-b pb-2">Budget Tracker</h3>
                            {budgetTracker && (
                                <>
                                    <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
                                        <div className="bg-blue-600 h-3 rounded-full" style={{ width: `${(budgetTracker.spent / budgetTracker.total) * 100}%` }}></div>
                                    </div>
                                    <p className="text-gray-700 text-sm">Spent: <span className="font-semibold">{budgetTracker.currency}{budgetTracker.spent}</span> / {budgetTracker.currency}{budgetTracker.total}</p>
                                </>
                            )}
                        </div>
                    </div>
                </div>

                {/* Footer buttons */}
                <div className="flex flex-col sm:flex-row justify-end mt-8 space-y-3 sm:space-y-0 sm:space-x-4">
                    <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg shadow-md transition duration-300 ease-in-out">Download Full Itinerary (PDF)</button>
                    <button className="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-3 px-6 rounded-lg shadow-md transition duration-300 ease-in-out">Share Trip with Friends</button>
                    <button className="bg-red-500 hover:bg-red-600 text-white font-bold py-3 px-6 rounded-lg shadow-md transition duration-300 ease-in-out">Cancel / Refund Options</button>
                </div>
            </div>
        </div>
    );
}

export default TripOverview;
