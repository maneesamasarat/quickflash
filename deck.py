from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user

from models import db, Card, Deck
from util import error, message

blueprint = Blueprint('deck', __name__)


def find_deck_or_fail(deck_id):
    deck = Deck.query.filter_by(id=deck_id, user_id=current_user.id).first()
    if not deck:
        abort(error("Deck not found.", 404))
    return deck


@blueprint.route('/decks')
@login_required
def index():
    return jsonify({
        'decks': list(reversed(current_user.decks))
    })


@blueprint.route('/decks/<int:deck_id>')
@login_required
def show(deck_id):
    deck = find_deck_or_fail(deck_id)
    return jsonify({
        'deck': deck,
        'cards': deck.cards
    })


@blueprint.route('/decks/<int:deck_id>/export')
@login_required
def export(deck_id):
    from jobs import export_deck
    deck = find_deck_or_fail(deck_id)
    export_deck.delay(deck.id)
    return message("Deck export initiated. You will receive an email at " + deck.user.email + " when it is ready.")


@ blueprint.route('/decks', methods=['PUT'])
@ blueprint.route('/decks/<int:deck_id>', methods=['PUT'])
@ login_required
def store(deck_id=None):
    name = request.form.get('name', current_user.name + "'s Deck")
    card_ids = request.form.getlist('card_ids[]')
    scores = request.form.getlist('score[]')
    front_sides = request.form.getlist('front[]')
    back_sides = request.form.getlist('back[]')

    if deck_id:
        deck = find_deck_or_fail(deck_id)
        deck.name = name
    else:
        deck = Deck(user_id=current_user.id, name=name)

    i = 0
    num_cards = len(deck.cards)

    while i < num_cards:
        if (str(deck.cards[i].id) in card_ids):
            form_card_index = card_ids.index(str(deck.cards[i].id))
            card_ids.pop(form_card_index)
            deck.cards[i].front = front_sides.pop(form_card_index)
            deck.cards[i].back = back_sides.pop(form_card_index)
            deck.cards[i].points = scores.pop(form_card_index)
            db.session.commit()
            i += 1
        else:
            deck.cards.pop(i)
            num_cards -= 1

    new_cards = [Card(front=front_sides[i], back=back_sides[i],
                      points=scores[i]) for i in range(len(card_ids))]

    deck.cards.extend(new_cards)

    if not deck_id:
        db.session.add(deck)

    db.session.commit()

    return jsonify({
        "message": "Deck {} successfully.".format("updated" if deck_id else "created"),
        "deck": deck

    }), 200 if deck_id else 201


@ blueprint.route('/decks/<int:deck_id>', methods=['DELETE'])
@ login_required
def destroy(deck_id):
    deck = find_deck_or_fail(deck_id)

    db.session.delete(deck)
    db.session.commit()

    return message("Deck deleted successfully.")
