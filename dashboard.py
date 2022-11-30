from flask import Blueprint , jsonify
from flask_login import login_required, current_user

blueprint = Blueprint('dashboard', __name__)


@blueprint.route('/')
@login_required
def index():
    return jsonify({
        'decks': list(reversed(current_user.decks))
    })
