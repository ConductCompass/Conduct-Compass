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

def get_all_reviews():
     return Review.query.all()

def get_all_reviews_json():
     reviews = Review.query.all()
     if not reviews:
        return []
     reviews = [review.get_json() for review in reviews]
     return reviews

def update_review_upvotes(reviewID):
     review = Review.query.filter_by(reviewID=reviewID).first()
     if review:
          review.upvotes = review.upvotes + 1
          db.session.add(review)
          db.session.commit()
