"use client";

import Image from "next/image";
import { UserAuth } from "@/context/AuthContext";
import LandingSide from "./components/LandingSide";
import { useRouter } from "next/navigation";
import { useState, useEffect } from "react";

export default function Home() {
  const { user, googleSignIn, signOutUser } = UserAuth();
  const router = useRouter();

  const handleSignIn = async () => {
    try {
      await googleSignIn();
      router.push("/dashboard");
    } catch (error) {
      console.log(error);
    }
  };

  const redirectToDash = () => {
    router.push("/dashboard");
  };

  return (
    <div className="w-full h-screen flex bg-white">
      <LandingSide />
      <div className="flex items-center justify-center w-1/2 relative h-full bg-white">
        <div className="flex flex-col items-center justify-center gap-2 border p-10 rounded-md">
          <span className=" flex gap-3 items-center justify-center pb-4">
            <Image src="/blue.png" width={100} height={100} className="" />
            <h3 className="font-semibold text-[#3182CE] text-4xl">Mirai</h3>
          </span>
          <button
            className="border-gray-300 border-[1px] text-black font-semibold py-3 px-10  rounded-md flex items-center gap-2 justify-center"
            onClick={user ? redirectToDash : handleSignIn}
          >
            <Image
              src={user && user.photoURL ? user.photoURL : "/google.png"}
              width={20}
              height={20}
              className="rounded-full shadow-md"
            />
            {user ? "Acessar dashboard" : "Login com Google"}
          </button>
          {user && (
            <button onClick={signOutUser} className="text-sm">
              Sign out!
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
