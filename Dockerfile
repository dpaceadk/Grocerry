# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /django

# Install dependencies
COPY ./requirements.txt /django/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /django

# Expose port 8000 to the Docker host
EXPOSE 8000

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
