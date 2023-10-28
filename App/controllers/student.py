from App.models import Student
from App.database import db
from App.config import config 
from flask import request, jsonify
from datetime import datetime

def add_student(studentID, name, dob, degree):
    dob_datetime = datetime.fromisoformat(dob)
    newstudent = Student(studentID=studentID, name=name, dob=dob_datetime, degree=degree)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent 

def search_student(studentID): 
    student = Student.query.filter_by(studentID=studentID).first()

    if student:
        return student.get_json()
    else:
        return None

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [student.get_json() for student in students]
    return students


def update_student(studentID, score): 
    student = Student.query.filter_by(studentID=studentID).first()
    
    if student:
        student.score = score
        db.session.add(student)
        db.session.commit()


def update_reviews_received(studentID): 
    student = Student.query.filter_by(studentID=studentID).first()
    
    if student:
        student.reviews_received = student.reviews_received + 1
        db.session.add(student)
        db.session.commit()

def get_student(studentID): 
    student = Student.query.filter_by(studentID=studentID).first()
    
    if student:
        return student
    else:
        return None

