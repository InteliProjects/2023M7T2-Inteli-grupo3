FROM node:18-alpine

# Set environment variables
ENV NEXT_PUBLIC_UPLOAD_URL=http://localhost:5000/upload
ENV NEXT_PUBLIC_PREDICT_URL=http://localhost:5000/predict
ENV NEXT_PUBLIC_STREAMLIT_URL=http://localhost:8501/

WORKDIR /app

COPY ../frontend/package.json ./

RUN npm install

COPY ../frontend .

CMD ["npm", "run", "dev"]