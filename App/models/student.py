from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    dob = db.Column(db.DateTime, nullable = False)
    degree = db.Column(db.String(120))
    reviews_received = db.Column(db.Integer)
    score = db.Column(db.Integer)
