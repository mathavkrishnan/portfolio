# Use an official Python runtime as a parent image
FROM python:3.11-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory in the container
WORKDIR /portfolio
# Copy the current directory contents into the container at /app
COPY . /portfolio/
# Copy the requirements.txt file
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Collect static files
RUN python manage.py collectstatic --no-input
# Expose the port the app runs on
EXPOSE 8000
# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0", "portfolio.wsgi:application"]
