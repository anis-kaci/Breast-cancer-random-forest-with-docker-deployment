# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r reqs.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable for the model file
ENV MODEL_FILE model.pkl

# Run app.py when the container launches
CMD ["python", "app.py"]