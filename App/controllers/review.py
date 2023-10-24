from App.models import Review, Student, Staff
from App.database import db
from App.config import config
from flask import jsonify, request
from App.controllers.staff import (update_num_reviews)
from App.controllers.student import (update_reviews_received)

def log_review(reviewID, studentID, staffID, comments, upvotes, downvotes):
     review = Review(reviewID=reviewID, studentID=studentID, staffID=staffID, comments=comments, upvotes=upvotes, downvotes=downvotes)

     #update_num_reviews(staffID)
     #update_reviews_received(studentID)

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

def update_review_downvotes(reviewID):
     review = Review.query.filter_by(reviewID=reviewID).first()
     if review:
          review.downvotes = review.downvotes + 1
          db.session.add(review)
          db.session.commit()
