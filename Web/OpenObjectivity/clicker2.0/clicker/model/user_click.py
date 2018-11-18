from .. import app

db = app.db


class UserClicker(db.Model):

    __tablename__ = 'user_clicker'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    uuid = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=1)

    def __repr__(self):
        return str({'name': self.name,
                    'quantity': self.quantity})
