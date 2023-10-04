from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Review(db.Model):
    reviewID = db.Column (db.Integer, primary_key = True)
    studentID= db.Column (db.Integer, db.ForeignKey ('student.studentID'))
    staffID = db.Column (db.Integer, db.ForeignKey ('staff.staffID'))
    comments = db.Column (db.String(120), nullable = False)
    upvotes = db.Column (db.Integer)
    downvotes = db.Column (db.Integer)
