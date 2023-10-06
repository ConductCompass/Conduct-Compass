from App.models import Downvote
from App.database import db
from App.config import config
from flask import request
import json

def downvote_review(downvoteID, reviewID, staffID): #staffID of staff member that made downvote on the review
    downvote = Downvote(downvoteID=downvoteID, reviewID=reviewID, staffID=staffID)
    db.session.add(downvote)
    db.session.commit()
    return downvote 

def get_downvotes(): 
  downvotes = Downvote.query.all()
  return downvotes
  
