import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from .. import app
from ..config import key
from .blacklist import BlacklistToken

db = app.db


class Auth(db.Model):
    """ Auth Model for storing auth related details """
    __tablename__ = 'auth'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(100))
    uuid = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    last_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    brute_check = db.Column(db.Integer, default=0)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def encode_auth_token(self, user_id):
        try:
            curr_time = datetime.datetime.utcnow()
            payload = {
                'exp': curr_time + datetime.timedelta(days=1, seconds=5),
                'iat': curr_time,
                'sub': user_id,
                'admin': self.admin
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @staticmethod
    def admin_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key)
            return payload['admin']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<Auth '{}'>".format(self.username)
