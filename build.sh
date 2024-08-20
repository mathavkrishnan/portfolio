#!/bin/bash

# Collect static files
python3 manage.py collectstatic --no-input

# Run the Django development server
python3 manage.py runserver 0.0.0.0:8000
