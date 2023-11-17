'use client'

import React, {useState, useEffect} from 'react'
import Form from '../components/Form'
import Sidebar from '../components/Sidebar'


const page = () => {
    const [days, setDays] = useState('?')
    

    return (
      <div className="flex h-full bg-gradient-to-b from-[#3182CE] to-blue-300">
        <Sidebar />
        <div className="flex flex-col justify-center items-center m-4 rounded-md p-2 bg-white">
            <h1 className='text-[#3182CE] text-2xl font-semibold pb-5 pt-8'>Dias até a próxima falha: {days}</h1>
            <Form setDays={setDays}/>
        </div>
        
      </div>
    );
  };
  
  export default page;
  
  