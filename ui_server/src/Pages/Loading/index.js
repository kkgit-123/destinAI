import * as React from "react";
import { InfinitySpin } from "react-loader-spinner";
function Loading() {
    

  return (
    <>
      <div className=" flex h-[100%] w-[100%]  justify-center items-center transform -rotate-45 -rotate-y-45%">
      <InfinitySpin width="300" color="#FF6005" />
      </div>
    </>
  );
}

export default Loading;
