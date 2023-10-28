from App.models import Upvote
from App.database import db
from App.config import config
from flask import request
import json


def upvote_review(upvoteID, reviewID, staffID): #staffID of staff member that made upvote on the review
    upvote = Upvote(upvoteID=upvoteID, reviewID=reviewID, staffID=staffID)
    db.session.add(upvote)
    db.session.commit()
    return upvote 

def get_upvotes(): 
    upvotes = Upvote.query.all()
    return upvotes

def get_upvotes_json(): 
    upvotes = Upvote.query.all()
    
    if not upvotes:
        return []
    
    upvotes = [upvote.get_json() for upvote in upvotes]
    return upvotes
  
