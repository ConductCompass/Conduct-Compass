from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Upvote(db.Model):
    upvoteID = db.Column(db.Integer, primary_key = True)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    reviewID = db.Column(db.Integer, db.ForeignKey('review.reviewID'))
