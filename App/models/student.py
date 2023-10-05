from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    dob = db.Column(db.DateTime, nullable = False)
    degree = db.Column(db.String(120))
    reviews_received = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, studentID, name, dob, degree, reviews_received, score):
        self.studentID = studentID
        self.name = name
        self.dob = dob
        self.degree = degree
        self.reviews_received = reviews_received
        self.score = score

    def get_json(self): 
        return{
            'studentID': self.studentID,
            'name': self.name,
            'dob': self.dob,
            'degree': self.degree,
            'reviews_received': self.reviews_received, 
            'score': self.score
        }
            
