import os
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

from main import app

import auth
import dashboard
import deck
import review

from models import db, User
from util import message

load_dotenv()

# Seed database and user
if not os.path.exists(app.config["SQLALCHEMY_DATABASE_URI"].split("///")[1]):
    db.create_all()
    user = User(
        email='test-user@gmail.com',
        name='Test User',
        password=generate_password_hash('test@123', method='sha256')
    )
    db.session.add(user)
    db.session.commit()

# Register blueprints
app.register_blueprint(dashboard.blueprint, url_prefix='/api')
app.register_blueprint(auth.blueprint, url_prefix='/api')
app.register_blueprint(deck.blueprint, url_prefix='/api')
app.register_blueprint(review.blueprint, url_prefix='/api')


# Intiailize login manager

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.request_loader
def load_user_from_request(request):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(' ')[1]
        user = User.query.filter_by(token=token).first()
        if user:
            return user
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return message('Please log in again.', 401)


# Clear cache and start app
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=os.getenv('PORT', 5000),
        debug=True,
        threaded=True
    )
