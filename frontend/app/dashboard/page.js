'use client'

import Sidebar from "../components/Sidebar";
import Image from "next/image";
import Cards from "../components/Cards";
import { useEffect, useState } from "react";
import { UserAuth } from "@/context/AuthContext";

import { useRouter } from "next/navigation";

const page = () => {
  const { user} = UserAuth();
  const router = useRouter();
  const [streamlitUrl, setStreamlitUrl] = useState("localhost");
  useEffect(() => {
    setStreamlitUrl(process.env.NEXT_PUBLIC_STREAMLIT_URL)
    if (!user) {
      router.push("/");
    }
  }, [])

  return (
    <div className="flex h-screen bg-white">
      <Image
        src="/bg.png"
        layout="responsive"
        width={1920}
        height={200}
        className="absolute"
        border_radius={0}
      />
      <Sidebar />
      <div className="w-full flex flex-col gap-5 pr-3 h-screen">
        <div className="flex justify-center w-full z-10">
          <Cards />
        </div>
        <span className="-ml-2 flex w-full justify-center z-10 h-full">
        <iframe
        width="100%"
        height="100%"
        src={`http://${streamlitUrl}:8501`}
        
        
      />
        </span>
      </div>
    </div>
  );
};

export default page;
