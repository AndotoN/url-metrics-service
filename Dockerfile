# Use a lightweight Python base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory's contents into the container's /app directory
COPY . .

# Install required Python libraries
RUN pip install --no-cache-dir prometheus-client requests

# Expose the port used by the metrics server
EXPOSE 8000

# Define the command to run the application
CMD ["python", "url_metrics.py"]
