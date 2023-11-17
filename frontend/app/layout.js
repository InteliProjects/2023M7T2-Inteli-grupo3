import "./globals.css";
import { Lato } from "next/font/google";
import { Anton } from "next/font/google";
import { AuthContextProvider } from "@/context/AuthContext";

const lato = Lato({
  subsets: ["latin"],
  weight: "400",
  variable: "--font-anton",
});

export const metadata = {
  title: "Mirai",
  description: "Manutenção preditiva para a Azul",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${lato.variable}`}>
        <AuthContextProvider>{children}</AuthContextProvider>
      </body>
    </html>
  );
}
