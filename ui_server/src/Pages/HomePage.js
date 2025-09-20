import React from 'react';
import Header from '../components/Header';
import FlightSearch from '../components/FlightSearch';
import ExclusiveOffers from '../components/ExclusiveOffers';

const HomePage = () => {
    return (
        <div className='flex flex-col h-screen w-screen overflow-hidden'>
            <div className='flex flex-col w-screen h-[8%]'>
                <Header />
                </div>
            <div className='flex flex-col w-screen h-[35%]'>
                <FlightSearch />
                </div>
            <div className='flex flex-col w-screen h-[50%]'>
                <ExclusiveOffers />
                </div>
        </div>
    );
};

export default HomePage;
