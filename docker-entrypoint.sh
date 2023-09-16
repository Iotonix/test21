#!/bin/bash
cd /src
echo "ENTRY POINT FOR DOCKER"
pip install greenlet
pip install gevent
ls -l
# Collect static files
echo "Collect static files"

python manage.py collectstatic --noinput
ls -l static

# Make database migrations
echo "Make database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=winner
export DJANGO_SUPERUSER_EMAIL=dev@winstantpay.com
export DJANGO_SUPERUSER_PASSWORD=lingo22+mitre

python3 manage.py createsuperuser --noinput 

# Start server
echo "Starting server now"
gunicorn lingo.wsgi -b 0.0.0.0:8000 --worker-class=gevent --worker-connections=10 --workers 2

