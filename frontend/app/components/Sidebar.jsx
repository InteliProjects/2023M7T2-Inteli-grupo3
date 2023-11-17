"use client";
import Image from "next/image";
import { useState } from "react";
import { AiFillHome } from "react-icons/ai";
import { BsFillCloudUploadFill } from "react-icons/bs";
import { useRouter } from "next/navigation";
import { UserAuth } from "@/context/AuthContext";
import {RiFlightTakeoffLine} from "react-icons/ri";

const Sidebar = () => {
  const [selectedItem, setSelectedItem] = useState("/dashboard");
  const { user, googleSignIn, signOutUser } = UserAuth();
  const router = useRouter();

  const handleItemClick = (item) => {
    setSelectedItem(item);
    router.push(item);
  };
  return (
    <div className="bg-white rounded-lg w-1/4 px-4 py-4 m-4 shadow-md relative">
      <span className=" flex gap-3 items-center justify-center pb-4">
        <Image src="/blue.png" width={50} height={50} className="" />
        <h3 className="font-semibold text-[#3182CE] text-2xl">Mirai</h3>
      </span>
      <hr />
      <div className="space-y-2 flex flex-col pt-4">
        <span
          className={`p-2 text-sm font-semibold flex items-center justify-center gap-2 ${
            selectedItem === "/dashboard" ? "shadow-md" : "hover:text-[#3182CE]"
          } rounded cursor-pointer transition duration-300`}
          onClick={() => handleItemClick("/dashboard")}
        >
          <span
            className={`${
              selectedItem === "/dashboard"
                ? "bg-[#3182CE] text-white"
                : "hover:text-[#3182CE]"
            } rounded-md p-1`}
          >
            <AiFillHome />
          </span>
          Home
        </span>
        <span
          className={`p-2 text-sm font-semibold flex items-center justify-center gap-2 ${
            selectedItem === "/upload" ? "shadow-md" : "hover:text-[#3182CE]"
          } rounded cursor-pointer transition duration-300`}
          onClick={() => handleItemClick("/upload")}
        >
          <span
            className={`${
              selectedItem === "/upload"
                ? "bg-[#3182CE] text-white"
                : "hover:text-[#3182CE]"
            } rounded-md p-1`}
          >
            <BsFillCloudUploadFill />
          </span>
          Upload
        </span>
        <span
          className={`p-2 text-sm font-semibold flex items-center justify-center gap-2 ${
            selectedItem === "/upload" ? "shadow-md" : "hover:text-[#3182CE]"
          } rounded cursor-pointer transition duration-300`}
          onClick={() => handleItemClick("/predict")}
        >
          <span
            className={`${
              selectedItem === "/upload"
                ? "bg-[#3182CE] text-white"
                : "hover:text-[#3182CE]"
            } rounded-md p-1`}
          >
            <RiFlightTakeoffLine />
          </span>
          Predict
        </span>
      </div>
      <span className="flex absolute bottom-4 items-center justify-between gap-2">
        <img
          src={user?.photoURL}
          width={40}
          height={40}
          style={{
            borderRadius: "50%",
            width: "40px",
            height: "40px",
          }}
          alt="User Avatar"
        />

        <p className="font-semibold text-sm">{user?.displayName}</p>
      </span>
    </div>
  );
};

export default Sidebar;
