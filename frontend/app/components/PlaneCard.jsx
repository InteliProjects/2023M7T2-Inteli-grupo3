import { LuPlane } from "react-icons/lu";

const PlaneCard = () => {
  return (
    <div className="bg-white p-2 rounded-lg w-48 h-20 shadow-md flex justify-between items-center">
      <div>
        <p className="text-gray-500 font-semibold text-sm flex items-start ">
          AERONAVE
        </p>
        <p className="text-black font-semibold text-sm flex items-start">
          40 horas
        </p>
      </div>
      <span className="text-gray-500 text-3xl">
        <LuPlane />
      </span>
    </div>
  );
};

export default PlaneCard;
