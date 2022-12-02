from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from models import db, User
from util import error

blueprint = Blueprint('auth', __name__)


def generate_token(user):
    token = user.email + user.password + str(datetime.now())
    user.token = generate_password_hash(token, method='sha256')
    db.session.commit()
    return user.token

#Check if the DB already has a user with the email provided before creating a new user in the DB
@blueprint.route('/auth/register', methods=['POST'])
def store():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user:
        return error('User already exists.')

    user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method='sha256')
    )

    generate_token(user)

    db.session.add(user)
    db.session.commit()

    return jsonify(user)

#Incorrect credentials
@blueprint.route('/auth/login', methods=['POST'])
def authenticate():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return error('Invalid email or password.')

    generate_token(user)
    
    return jsonify(user)