from App.models import KarmaScore
from App.database import db
from App.config import config
import requests 
import json

def calculate_karma_score(username):
    score = Score.query.filter_by(username= username).first()
    if score:
        return score
    return None
