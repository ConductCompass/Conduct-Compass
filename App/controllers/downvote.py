from App.models import Downvote
from App.database import db
from App.config import config
from flask import request
import json

def get_downvotes(): 
  return downvotes.get_json()
  

#def downvote_review(): 
