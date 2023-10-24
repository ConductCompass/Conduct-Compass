from App.models import KarmaScore, Student, Review
from App.controllers.student import update_student
from App.database import db
from App.config import config
import requests 
import json

def calculate_karma_score(studentID):
    score = 0
    reviews = Review.query.All()

    for review in reviews:
        if review.studentID == studentID:
            score = score + (review.upvotes - review.downvotes) 

    update_student(studentID, score)
            
    return score
 
