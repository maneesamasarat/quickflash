#!/bin/bash
sudo service redis-server start 
(cd client && npx vite build)
source .venv/bin/activate
celery -A jobs.celery worker --loglevel INFO &
celery -A jobs.celery beat --loglevel INFO &
python app.py