from flask import Blueprint , jsonify
from flask_login import login_required, current_user

blueprint = Blueprint('dashboard', __name__)

# Render dashboard data
@blueprint.route('/')
@login_required
def index():
    return jsonify({
        'decks': list(reversed(current_user.decks))
    })
