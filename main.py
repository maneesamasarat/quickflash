import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from dotenv import load_dotenv

from celery_maker import make_celery

load_dotenv()

app = Flask(
    __name__,
    static_url_path='',
    static_folder='client/dist',
    template_folder='templates'
)

app.secret_key = os.getenv('SECRET_KEY')

# DB Config
app.config.update(
    SQLALCHEMY_DATABASE_URI=os.getenv(
        "DATABASE_URL", "sqlite:///quickflash.sqlite3"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# CORS, disable later
# CORS(app)

# Celery config
app.config.update(
    CELERY_BROKER_URL=os.getenv("REDIS_URL", "redis://127.0.0.1:6379"),
    CELERY_RESULT_BACKEND=os.getenv("REDIS_URL", "redis://127.0.0.1:6379"),
    CELERY_TIMEZONE="Asia/Kolkata",
)

# Initiate celery
celery = make_celery(app)

# Email config
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USERNAME=os.getenv('GMAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('GMAIL_PASSWORD'),
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_DEFAULT_SENDER=("QuickFlash Bot", os.getenv('GMAIL_USERNAME')),
)
mail = Mail(app)


@app.errorhandler(404)
def default_page(e):
    return app.send_static_file("index.html"), 200
