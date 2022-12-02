<br>
<h1>⚡ QuickFlash</h1>
QuickFlash is a modern and minimal flashcard app that enables users to train their memory and track their progress over time. Users can add decks (with cards inside them) and take reviews for each deck. It features a slick user interface and experience that makes using this application a breeze.

## Requirements
Primary requirements to run this project are Docker and VScode.

## Installation
Create the environment variables file **.env**:
```bash
SECRET_KEY="<Your_Secret_Key>"
PORT=5000
DATABASE_URL="sqlite:///quickflash.sqlite3" # Created automatically
REDIS_URL="redis://127.0.0.1:6379" # Default Redis URL
GMAIL_USERNAME="<Your_Email>@gmail.com" # Access for "Less secure apps" must be enabled for the Google Account
GMAIL_PASSWORD="<Your_Password>"
```
### Creating the container
Start Docker desktop app.
Start VS code.
Right click on **docker-compose.yml** and click on compose up.
## First use
By default, this app starts on http://localhost:8000. You may create your own account or use the following credentials.
<blockquote>
Email: <b>test-user@gmail.com</b><br />
Password: <b>test@123</b><br />
</blockquote>