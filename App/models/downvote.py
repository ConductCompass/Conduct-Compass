from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Downvote(db.Model):
    downvoteID = db.Column(db.Integer, primary_key = True)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    reviewID = db.Column(db.Integer, db.ForeignKey('review.reviewID'))

    def __init__(self, downvoteID, staffID, reviewID):
        self.downvoteID = downvoteID
        self.staffID = staffID
        self.reviewID = reviewID


    def get_json(self): 
        return{
            'downvoteID': self.downvoteID, 
            'staffID': self.staffID, 
            'reviewID': self.reviewID
        }
