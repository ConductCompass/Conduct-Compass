from App.models import Staff
from App.controllers import user
from App.database import db
from App.config import config 
from flask import request, jsonify

def create_staff(username, password):
    newuser = Staff(username=username, password=password)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except:
        return None

def get_staff(id):
    return Staff.query.get(id)

def get_all_staff():
    return Staff.query.all()

def get_all_staff_json():
    users = Staff.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users 


def update_num_reviews(staffID):
    staff = Staff.query.get(staffID)
    
    if staff:
            # Increment the "reviews_logged" attribute
            staff.reviews_logged = staff.reviews_logged + 1

            db.session.commit()
            return True
    else:
        return False 