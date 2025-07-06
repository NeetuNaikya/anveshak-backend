FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential gcc

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 8000

# Start the app (change if your main file or command is different)
CMD ["python", "src/app.py"]