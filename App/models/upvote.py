from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Upvote(db.Model):
    upvoteID = db.Column(db.Integer, primary_key = True)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    reviewID = db.Column(db.Integer, db.ForeignKey('review.reviewID'))

    def __init__(self, upvoteID, staffID, reviewID): 
        self.upvote = upvote
        self.staffID = staffID
        self.reviewID = reviewID

    def get_json(self): 
        return{
            'upvote': upvote,
            'staffID': staffID, 
            'reviewID': reviewID
        }
