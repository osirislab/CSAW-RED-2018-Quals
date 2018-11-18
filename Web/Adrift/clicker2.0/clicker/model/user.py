import datetime

from .. import app

db = app.db


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = 'user'

    uuid = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(255), unique=True)
    money = db.Column(db.Integer, default=5)
    record_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    record = db.Column(db.Integer, default=0)
