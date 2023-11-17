import React from "react";
import PlaneCard from "./PlaneCard";

const Cards = () => {
  return (
    <div className="w-full pt-6 ">
        <h3 className="text-white font-semibold text-2xl">Dashboard</h3>
      <div className="flex w-full justify-between pt-6">
        <PlaneCard />
        <PlaneCard />
        <PlaneCard />
        <PlaneCard />
      </div>
    </div>
  );
};

export default Cards;
