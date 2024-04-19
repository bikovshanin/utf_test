#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

python manage.py migrate

python manage.py seed
echo "Seed completed. Data loaded successfully."

gunicorn backend.wsgi --bind 0.0.0.0:8000
