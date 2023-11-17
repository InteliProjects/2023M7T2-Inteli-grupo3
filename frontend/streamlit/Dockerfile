# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ../frontend/streamlit/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ../frontend/streamlit /app/

# Expose port 8501 for Streamlit
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "dashboard.py"]
