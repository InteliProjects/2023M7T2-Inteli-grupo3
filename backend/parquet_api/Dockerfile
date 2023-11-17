# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for FastAPI
ENV PORT=8000
ENV HOST=0.0.0.0

# Create and set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./backend/parquet_api/ /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define the command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
