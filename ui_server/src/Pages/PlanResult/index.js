import React, { useState, useEffect, useMemo } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import BlueLoaderOverlay from './BlueLoaderOverlay';
import Chat from "../../components/Chat";
import DisplayPlan from "../../components/DisplayPlan";
import ThemedHeader from '../../components/ThemedHeader'; // Import ThemedHeader
import Breadcrumbs from "../../components/Breadcrumbs"; // Importing Breadcrumbs component
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa'; // Importing icons
import planData from '../../constants/planData'; // Import planData as fallback
import { ENDPOINTS } from '../../constants/endpoints';
import MapView from "../../components/MapView"; // Import MapView
import { useLoadScript } from '@react-google-maps/api'; // Import useLoadScript

import logo from "../../Images/favicon.ico"
function PlanResult() {
    const { planId } = useParams();
    const navigate = useNavigate();
    const [isChatCollapsed, setIsChatCollapsed] = useState(false);
    const [isLoading, setIsLoading] = useState(false); // New loading state
    const [currentPlanData, setCurrentPlanData] = useState(null); // Initialize with null, will be set by fetch
    const [selectedLocations, setSelectedLocations] = useState([]); // State to hold locations for the selected day

    const { isLoaded, loadError } = useLoadScript({
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
        libraries: ["places"], // Add any necessary libraries
    });

    useEffect(() => {
        const fetchPlanData = async () => {
            let dataToUse = planData; // Default to local fallback

            if (planId) {
                try {
                    const response = await fetch(`${ENDPOINTS.PLAN_DATA}/${planId}`);
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    dataToUse = await response.json();
                } catch (error) {
                    console.error("Failed to fetch plan data:", error);
                    alert("Failed to load plan data from server. Using local data.");
                }
            } else {
                console.warn("No planId found, using local data.");
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
    }, [planId]);

    const toggleChat = () => {
        setIsChatCollapsed(!isChatCollapsed);
    };

    const handleConfirmPlan = async () => {
        setIsLoading(true); // Set loading to true
        console.log("Confirming plan...");
        await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate 2-second API call
        const tripId = planId; 
        console.log(`Plan confirmed, navigating to /trip-overview/${tripId}`);
        setIsLoading(false); // Set loading to false
        navigate(`/trip-overview/${tripId}`);
    };

    const handleDayClick = (locations) => {
        setSelectedLocations(locations);
    };

    const filteredTabs = ["Itinerary", "Food", "Bookings", "Suggestions", "Locations"];

    const MapComponent = useMemo(() => {
        if (loadError) return <div>Error loading maps</div>;
        if (!isLoaded) return <div>Loading Maps...</div>;
        return <MapView spots={selectedLocations} />;
    }, [isLoaded, loadError, selectedLocations]);


    return (
        <>
            <div className=" flex  flex-col h-screen w-screen">
                <div className='flex w-screen h-[8%] mb-1'>
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
                    <Breadcrumbs currentStep={2} />
                </div>
                <div className="flex  h-[86%] rounded-lg mx-2 mb-2  ">
                    <div className={`flex mr-2 ${isChatCollapsed ? 'w-[99%]' : 'w-[70%]'} h-[100%] rounded-lg bg-gray-200`}>
                        {currentPlanData ? (
                            <DisplayPlan planData={currentPlanData} filteredTabs={filteredTabs} onDayClick={handleDayClick} MapComponent={MapComponent} />
                        ) : (
                            <div className="flex items-center justify-center w-full h-full text-gray-500">
                                Loading plan data...
                            </div>
                        )}
                    </div>
                    <div className={`relative flex ${isChatCollapsed ? 'w-[0%] overflow-hidden' : 'w-[30%]'} h-[100%] rounded-lg bg-gray-200 transition-all duration-300 ease-in-out`}>

                        <div className={`${isChatCollapsed ? 'hidden' : 'block'} w-full h-full`}>
                            <div className="flex justify-end ">
                                {isLoading ? (
                                    <BlueLoaderOverlay />
                                ) : (
                                    <button
                                        onClick={handleConfirmPlan}
                                        className="bg-green-500 text-white px-6 py-1 rounded-md text-sm font-bold  transition-colors duration-300 transform cursor-pointer transition-transform duration-300 p-4 hover:scale-105"
                                    >
                                        Confirm Plan
                                    </button>
                                )}
                            </div>
                            <Chat />
                        </div>
                    </div>
                    <button
                        onClick={toggleChat}
                        className={`absolute top-1/8  text-black p-1 rounded-full  z-10 ${isChatCollapsed ? 'right-0' : 'right-[29%]'} transition-all duration-300 ease-in-out`}
                    >
                        {isChatCollapsed ? <FaChevronLeft /> : <FaChevronRight />}
                    </button>
                </div>
            </div>
        </>
    );
}

export default PlanResult;
