import Image from "next/image"
const LandingSide = () => {
  return (
    <div className='p-4 w-1/2 h-full'>
        <div className="bg-gradient-to-b from-[#3182CE] to-blue-300 relative rounded-xl h-full flex justify-center items-center">
            <Image src='/deco.png' className="absolute bottom-0 left-0" width={300} height={300}/>
            <div className="bg-opacity-25 backdrop-blur-md rounded-lg p-4 bg-blue-300 h-4/5 w-2/3 relative border">
                <h1 className="text-white text-4xl font-semibold">Prepare-se<br/>
                para o futuro<br/>
                com Mirai!</h1>
                <Image src='/plane.png' className="absolute -bottom-24 -right-36 -rotate-9" width={800} height={400}/>
            </div>
        </div>
    </div>
  )
}

export default LandingSide