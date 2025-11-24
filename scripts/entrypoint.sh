#!/bin/bash

# Wait for postgres if needed (optional, or use wait-for-it)

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start the application
exec "$@"
