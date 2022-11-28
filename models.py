from dataclasses import dataclass
from main import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy(app)

#user table
@dataclass
class User(db.Model, UserMixin):
    id: int
    name: str
    email: str
    token: str

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(length=100))
    email = db.Column(db.Unicode(length=100), unique=True)
    password = db.Column(db.Text(length=72))
    token = db.Column(db.Text(length=100), nullable=True)

    decks = db.relationship('Deck', back_populates='user',
                            cascade="all, delete-orphan")
    reviews = db.relationship(
        'Review', back_populates='user', cascade="all, delete-orphan")


@dataclass
class Deck(db.Model):
    id: int
    name: str
    max_score: int
    last_review: dict

    __tablename__ = 'decks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.Unicode(length=100))

    user = db.relationship("User", back_populates="decks")

    cards = db.relationship('Card', back_populates='deck',
                            cascade="all, delete-orphan")
    reviews = db.relationship(
        'Review', back_populates='deck', cascade="all, delete-orphan")

    @property
    def max_score(self):
        return sum([4 * card.points for card in self.cards])

    @property
    def last_review(self):
        return self.reviews[-1] if len(self.reviews) > 0 else None


@dataclass
class Card(db.Model):
    id: int
    front: str
    back: str
    points: int
    max_score: int

    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    front = db.Column(db.Unicode(length=100))
    back = db.Column(db.Unicode(length=100))
    points = db.Column(db.Integer)

    deck = db.relationship("Deck", back_populates="cards")
    review_cards = db.relationship(
        "ReviewCard", back_populates="card", cascade="all, delete-orphan")

    @property
    def max_score(self):
        return self.points * 4


@dataclass
class Review(db.Model):
    id: int
    taken_at: str
    score: int
    max_score: int
    score_percent: float

    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    taken_at = db.Column(db.DateTime)

    cards = db.relationship(
        'ReviewCard', back_populates="review", cascade="all, delete-orphan")

    user = db.relationship("User", back_populates="reviews")
    deck = db.relationship("Deck", back_populates="reviews")

    @property
    def score(self):
        return sum([rc.score for rc in self.cards])

    @property
    def max_score(self):
        return sum([rc.card.points * 4 for rc in self.cards])

    @property
    def score_percent(self):
        return int(self.score * 100 / max(self.max_score, 1))


@dataclass
class ReviewCard(db.Model):
    id: int
    card: dict
    difficulty: int
    score: int
    score_percent: float

    __tablename__ = 'review_cards'
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))
    difficulty = db.Column(db.Integer)
    score = db.Column(db.Integer)

    review = db.relationship("Review")
    card = db.relationship("Card")

    @property
    def score_percent(self):
        return int(self.score * 100 / max(self.card.max_score, 1))
