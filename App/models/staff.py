from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Staff(db.Model):
    staffID = db.Column(db.Integer, primary_key = True)
    reviews_logged = db.Column(db.String(120))
