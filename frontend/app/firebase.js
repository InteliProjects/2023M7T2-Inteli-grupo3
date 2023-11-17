import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyD1-oHzlnFRVLbJM0L_YOrQ5APlIUNVPGc",
  authDomain: "mirai-21712.firebaseapp.com",
  projectId: "mirai-21712",
  storageBucket: "mirai-21712.appspot.com",
  messagingSenderId: "55933660747",
  appId: "1:55933660747:web:a30c485e4243edbc0067ce"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);