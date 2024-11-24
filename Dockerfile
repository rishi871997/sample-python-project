# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (optional if your app serves HTTP, remove if not needed)
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

