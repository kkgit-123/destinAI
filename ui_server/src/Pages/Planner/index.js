import mapBackground from "../../Images/map_bg.png";
import { FaPencilAlt } from "react-icons/fa";
import { FaRobot } from "react-icons/fa";
import { MdOutlineSave } from "react-icons/md";
import { FaHistory } from "react-icons/fa";
import { useNavigate } from 'react-router-dom';
import ThemedHeader from '../../components/ThemedHeader'; // Import ThemedHeader
import Breadcrumbs from '../../components/Breadcrumbs'; // Import Breadcrumbs

function Planner() {
  const navigate = useNavigate();

  return (
    <>
      <div className="flex flex-col h-screen w-screen bg-gray-100">
        <div className='flex w-screen h-[10%] mb-1'>  
            <ThemedHeader>
            <div className="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                    </svg>
                    <span className="font-bold text-lg text-gray-800">DestiniAI</span>
                </div>
         
            </ThemedHeader>
        </div>
        <div className="bg-white shadow-md w-full h-[5%] flex items-center justify-center">
           <Breadcrumbs currentStep={0} />
        </div>
       
        <div className="flex flex-col w-screen h-[81%] bg-cover bg-center bg-fit rounded-lg bg-white relative" style={{ backgroundImage: `url(${mapBackground})` }}>
          <div className="absolute inset-0 bg-white bg-opacity-80"></div> {/* Overlay for text readability */}
          <div className="relative z-10 flex flex-col items-center justify-center h-full p-4">
            <h1 className="text-4xl font-bold text-gray-800 mb-2">Embark on Your Adventure: How Will You Begin?</h1>
            <p className="text-gray-600 text-lg mb-8">Provide your vision or let our AI craft a personalized journey.</p>

            <div className="flex justify-center  space-x-8 mb-12">
              {/* I Know My Details Card */}
              <div className="flex flex-col w-[35%] cursor-pointer rounded-xl shadow-lg bg-white border border-gray-200 max-w-sm text-center transform transition-transform duration-300 hover:scale-105 hover:shadow-xl p-6 items-center justify-center"
                onClick={() => { navigate(`/plan/prompt`); }}
              >
                <div className="bg-blue-500 rounded-full p-4 text-white mb-4">
                  <FaPencilAlt size={30} />
                </div>
                <h3 className="text-xl font-bold text-gray-800 mb-2">Craft My Journey</h3>
                <p className="text-gray-700 text-sm">Input destinations, dates, budget, and preferences.</p>
              </div>

              {/* Help Me Plan Card */}
              <div className="flex flex-col w-[35%] cursor-pointer rounded-xl shadow-lg bg-white border border-gray-200 max-w-sm text-center transform transition-transform duration-300 hover:scale-105 hover:shadow-xl p-6 relative items-center justify-center"
                onClick={() => { navigate(`/plan/form`); }}
              >
                <div className="bg-blue-500 rounded-full p-4 text-white mb-4">
                  <FaRobot size={30} />
                </div>
                <h3 className="text-xl font-bold text-gray-800 mb-2">Inspire Me</h3>
                <p className="text-gray-700 text-sm">Answer a few questions, and we'll design your perfect itinerary.</p>
              </div>
            </div>

            <div className="flex flex-col items-center mb-8">
              <span className="text-gray-600 text-lg mb-4">Quick Access</span>
              <div className="flex space-x-8">
                <span className="flex text-blue-600 items-center cursor-pointer hover:underline">
                  <MdOutlineSave size={20} className="mr-2" />
                  My Saved Adventures
                </span>
                <span className="flex text-blue-600 items-center cursor-pointer hover:underline">
                  <FaHistory size={20} className="mr-2" />
                  Recent Explorations
                </span>
              </div>
            </div>

            <div className="flex items-center justify-between w-full max-w-2xl mt-auto">
              <span className="text-gray-600">Seeking Inspiration? Discover Curated <a href="#" className="text-blue-600 hover:underline">Journeys</a>.</span>
              <button className="bg-blue-600 text-white px-6 py-3 rounded-md hover:bg-blue-700">
                Continue
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Planner;
