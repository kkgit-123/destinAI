// import * as React from "react";
// import { InfinitySpin } from "react-loader-spinner";
// function Loading() {
    

//   return (
//     <>
//       <div className=" flex h-[100%] w-[100%]  justify-center items-center transform -rotate-45 -rotate-y-45%">
//       <InfinitySpin width="300" color="#FF6005" />
//       </div>
//     </>
//   );
// }

// export default Loading;


import React from 'react';
import Lottie from 'lottie-react';
import travelAnimation from '../../animations/loading.json'

export default function Loading() {
  return (
    <div className='flex h-screen w-screnn items-center justify-center'>
    <div style={{ width: 200, margin: 'auto' }}>
      <Lottie animationData={travelAnimation} loop={true} />
    </div>
    </div>
  );
}
