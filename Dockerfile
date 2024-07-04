# Use a base image with Python pre-installed
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Rasa project
COPY . .

# Set environment variables if necessary
ENV PORT 5005

# Expose the port on which Rasa server will run
EXPOSE ${PORT}

# Command to run Rasa server
CMD ["rasa", "run", "-p", "${PORT}", "--cors", "*"]