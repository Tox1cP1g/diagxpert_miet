# Use the official Python image as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /diagxpert_miet

# Install dependencies
COPY requirements.txt /diagxpert_miet
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project into the container
COPY . /diagxpert_miet/

# Run the Django project
CMD ["python", "manage.py", "runserver"]