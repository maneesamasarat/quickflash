from datetime import datetime
from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user
from deck import find_deck_or_fail
from util import error, message


blueprint = Blueprint('review', __name__)


def find_review_or_fail(review_id, deck_id):
    find_deck_or_fail(deck_id)
    review = Review.query.filter_by(id=review_id, deck_id=deck_id).first()
    if not review:
        abort(error("Review not found.", 404))
    return review


@blueprint.route('/decks/<int:deck_id>/reviews')
@login_required
def index(deck_id):
    deck = find_deck_or_fail(deck_id)
    deck.reviews.sort(key=lambda review: review.taken_at)
    deck.reviews.reverse()
    return jsonify({
        'deck': deck,
        'reviews': deck.reviews
    })


@blueprint.route('/decks/<int:deck_id>/reviews/<int:review_id>')
@login_required
def show(deck_id, review_id):
    review = find_review_or_fail(review_id, deck_id)
    review_cards = ReviewCard.query.filter_by(
        review_id=review_id).order_by(ReviewCard.score.asc()).all()

    return jsonify({
        'deck': review.deck,
        'review': review,
        'review_cards': review_cards,
    })


@blueprint.route('/decks/<int:deck_id>/reviews', methods=['POST'])
@login_required
def store(deck_id):
    find_deck_or_fail(deck_id)

    cards = request.form.getlist('cards[]')
    difficulties = request.form.getlist('difficulties[]')

    review = Review(user_id=current_user.id,
                    deck_id=deck_id, taken_at=datetime.now())

    for i in range(len(cards)):
        card = Card.query.filter_by(id=cards[i]).first()
        score = int(difficulties[i]) * int(card.points)
        review.cards.append(ReviewCard(
            card_id=cards[i], difficulty=difficulties[i], score=score))

    db.session.add(review)
    db.session.commit()

    return jsonify({
        'message': 'Review completed successfully.',
        'review': review
    })


@blueprint.route('/decks/<int:deck_id>/reviews/<int:review_id>', methods=['DELETE'])
@login_required
def destroy(deck_id, review_id):
    review = find_review_or_fail(review_id, deck_id)

    db.session.delete(review)
    db.session.commit()

    return message('Review deleted successfully.', 200)
