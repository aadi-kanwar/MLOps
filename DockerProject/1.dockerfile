# Use a base image with the desired operating system and dependencies
FROM python:3.9

# Set the working directory in the container
WORKDIR /DockerProject

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your project files to the container
COPY . .

# Set the command to run when the container starts
CMD ["python", "logistic.py"]
