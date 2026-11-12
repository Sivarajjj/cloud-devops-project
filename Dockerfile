
# Use Python as the base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose application port
EXPOSE 5000

# Start application
CMD ["python", "app.py"]
