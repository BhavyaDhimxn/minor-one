# Use the official Python image with a slim version for smaller size
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for required libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "minormain.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
