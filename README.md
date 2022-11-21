<br>
<h1>⚡ QuickFlash</h1>
QuickFlash is a modern and minimal flashcard app that enables users to train their memory and track their progress over time. Users can add decks (with cards inside them) and take reviews for each deck. It features a slick user interface and experience that makes using this application a breeze.

## Requirements
QuickFlash runs on Linux/Unix based OS-es with Python, NodeJS (with npm) and Redis installed. This guide assumes that all the requirements are fulfilled.

## Installation
Create the environment variables file **.env**:
```bash
SECRET_KEY="<Your_Secret_Key>"
PORT=80
DATABASE_URL="sqlite:///quickflash.sqlite3" # Created automatically
REDIS_URL="redis://127.0.0.1:6379" # Default Redis URL
GMAIL_USERNAME="<Your_Email>@gmail.com" # Access for "Less secure apps" must be enabled for the Google Account
GMAIL_PASSWORD="<Your_Password>"
```
Then,  run the following commands:
```bash
# Start Redis server
sudo service redis-server start 

# Install frontend dependencies and build static Vue app
(cd client && npm i && npx vite build)

# Initiate and activate the virtual environment
python3 -m venv .venv 
source .venv/bin/activate

# Install the backend dependencies
pip3 install -r requirements.txt

# Start Celery worker and Celery beat in the background
celery -A jobs.celery worker &
celery -A jobs.celery beat &

# Start the app
python3 ./app.py
```
## First use
By default, this app starts on http://localhost:5000. You may create your own account or use the following credentials.
<blockquote>
Email: <b>test-user@gmail.com</b><br />
Password: <b>test@123</b><br />
</blockquote>