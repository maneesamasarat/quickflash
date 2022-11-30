from asyncio.log import logger
from datetime import datetime, timedelta
import logging
import os
from io import StringIO
from flask_mail import Message
from flask import render_template
from main import celery, mail
from models import Deck, Review, User
from celery.schedules import crontab


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=19, minute=0),
        send_reminders.s(),
    )


@celery.task()
def export_deck(deck_id):

    import csv

    deck = Deck.query.get(deck_id)

    rows = [['Points', 'Front', 'Back']]

    for card in deck.cards:
        rows.append([card.points, card.front, card.back])

    stream = StringIO()

    writer = csv.writer(stream, quoting=csv.QUOTE_ALL)
    writer.writerows(rows)

    logging.info(f"Sending export email to {deck.user.email}")

    template_path = os.path.join(
        'emails',
        'export.html'
    )

    message = Message(
        subject="Your deck has been exported",
        html=render_template(template_path, user=deck.user),
        recipients=[deck.user.email],
    )

    message.attach("Deck.csv", "text/csv", stream.getvalue())
    mail.send(message)


@celery.task()
def send_reminders():
    midnight = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    users_who_reviewed = set(
        map(
            lambda review: review.user_id,
            Review.query.filter(Review.taken_at > midnight).all()
        )
    )

    users = User.query.filter(User.id.not_in(users_who_reviewed)).all()
    for user in users:
        send_reminder_to_user.delay(user.id)


@celery.task()
def send_reminder_to_user(id):
    user = User.query.get(id)

    logging.info(f"Sending reminder to {user.email}")

    template_path = os.path.join(
        'emails',
        'reminder.html'
    )

    reminder = Message(
        subject="Daily review reminder",
        html=render_template(template_path, user=user),
        recipients=[user.email],
    )

