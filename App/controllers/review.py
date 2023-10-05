from App.models import Review, Student, Staff
from App.database import db
from App.config import config
from flask import jsonify, request
import json 

def log_review(reviewID, studentID, staffID, comments, upvotes, downvotes):
     review = Review(reviewID=reviewID, studentID=studentID, staffID=staffID, comments=comments, upvotes=upvotes, downvotes=downvotes)
     db.session.add(review)
     db.session.commit()
     return review 

#def upvote_review(reviewID):

#def downvote_review(reviewID):