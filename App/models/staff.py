from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Staff(db.Model):
    staffID = db.Column(db.Integer, primary_key = True)
    reviews_logged = db.Column(db.String(120))
    staffName = db.Column(db.String(120))

    def __init__(self, staffID, reviews_logged): 
        self.staffID = staffID
        self.reviews_logged = reviews_logged
    
    def get_json(self): 
        return{
            'staffID': staffID,
            'staffName': staffName, 
            'reviews_logged': reviews_logged
        }
