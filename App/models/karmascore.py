from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class KarmaScore(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'))
    score = db.Column(db.Integer)

    def __init__(self, ID, studentID, score):
        self.ID = ID
        self.studentID = studentID
        self.score = score

    def get_json(self): 
        return{
            'ID': self.ID,
            'studentID': self.studentID, 
            'score': self.score
        }
