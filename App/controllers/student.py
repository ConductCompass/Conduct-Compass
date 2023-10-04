from App.models import Student
from App.database import db
from App.config import config 
import requests 
import json

def add_student(studentID, name, dob, degree): 
  newstudent = Student(studentId=studentId, name=name, dob=dob, degree=degree)
  db.session.add(newstudent)
  db.session.commit()
  return newstudent 

def update_student(studentID): 

def search_student(studentID): 

def get_student(studentID): 
