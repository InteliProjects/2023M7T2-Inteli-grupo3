/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        bg_blue: "#216DED",
      },
      fontFamily: {
        anton: "var(--font-anton)",
      },
    },
  },
  plugins: [require("daisyui")],
};
