# Usean official Node.js runtime as a parent image
FROM node:16 AS frontend

# Set the working directory to the frontend directory
WORKDIR /app/frontend

# Copy the package.json and package-lock.json files to the container
COPY frontend/package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY frontend/ ./

# Build the frontend application
RUN npm run build

# Use an official Python runtime as a parent image
FROM python:3.9 AS backend

# Set the working directory to the backend directory
WORKDIR /app/backend

# Copy the requirements file to the container
COPY backend/requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY backend/ ./

# Set environment variables
ENV FLASK_APP app.py
ENV FLASK_ENV production

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
