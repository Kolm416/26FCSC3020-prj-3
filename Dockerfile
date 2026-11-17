# CSC3020 - Software Engineering Fundamentals
# Instructor: Thyago Mota
# Student(s): Juvia Archuleta, Leigha Lennon
# Description: Project 3 - TaskTrack


# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python output immediately
ENV PYTHONUNBUFFERED=1

# Copy the dependency list into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY src/ ./src/

# Expose the Flask application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "-m", "flask", "--app", "src.app:app", "run", "--host=0.0.0.0", "--port=5000"]