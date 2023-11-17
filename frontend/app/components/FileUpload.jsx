'use client'
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FileUpload() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [uploadMessage, setUploadMessage] = useState('');
  const [uploadUrl, setUploadUrl] = useState('')

  useEffect(() => {
    setUploadUrl(process.env.NEXT_PUBLIC_UPLOAD_URL)
  }, [])

  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
    setUploadMessage('');
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      for (const file of selectedFiles) {
        formData.append('files', file);
      }

      setUploadMessage('Sending...'); // Set the "Sending..." message

      const response = await axios.post('54.166.245.51:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('Files uploaded successfully:', response.data);
      setUploadMessage('Files uploaded successfully!');
    } catch (error) {
      console.error('Error uploading files:', error);
      setUploadMessage('Error uploading files. Please try again.');
    }
  };

  return (
    <div className="bg-blue-100 p-4 rounded-lg shadow-lg">
      <label className="block text-blue-600 font-bold mb-2">Select Parquet Files</label>
      <input type="file" accept=".parquet" onChange={handleFileChange} multiple className="border rounded p-2 mb-4" />
      <button onClick={handleUpload} className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline-blue active:bg-blue-800">
        Upload
      </button>
      <p className={`mt-2 text-${uploadMessage.includes('successfully') ? 'green' : 'red'}-600 font-bold`}>
        {uploadMessage}
      </p>
    </div>
  );
}

export default FileUpload;
