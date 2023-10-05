from App.models import Student
from App.database import db
from App.config import config 
from flask import request
import json

def add_student(studentID, name, dob, degree, reviews_received, score):
    newstudent = Student(studentID=studentID, name=name, dob=dob, degree=degree, reviews_received=reviews_received, score=score)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent 

def search_student(studentID): 
    student = Student.query.filter_by(studentID=studentID).first()
    return student.get_json()

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [student.get_json() for student in students]
    return students


#def update_student(studentID): 

#def get_student(studentID): 


