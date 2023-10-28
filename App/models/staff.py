from App.database import db
from App.models import User
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

class Staff(User):
    staffID = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    reviews_logged = db.Column(db.Integer)

    __mapper_args__ = {
        'inherit_condition': (staffID == User.id)
    }

    def __init__(self, username, password):
        super().__init__(username, password)
        self.reviews_logged = 0

    def get_json(self):
        return {
            'staffID': self.staffID,
            'staffName': self.username,
            'reviews_logged': self.reviews_logged
        }