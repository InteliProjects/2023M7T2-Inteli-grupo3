'use client'
import Sidebar from "../components/Sidebar";
import { UserAuth } from "@/context/AuthContext";

import FileUpload from "../components/FileUpload";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

const page = () => {
  const { user} = UserAuth();
  const router = useRouter();

  useEffect(() => {
    if (!user) {
      router.push("/");
    }
  }, [])
    return (
      <div className="flex h-screen bg-gradient-to-b from-[#3182CE] to-blue-300">
        <Sidebar />
        <div className="flex justify-center items-center w-full h-full">
            <FileUpload/>
        </div>
        
      </div>
    );
  };
  
  export default page;
  