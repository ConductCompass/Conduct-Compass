from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (add_student, search_student, get_all_students, get_all_students_json, update_student)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/createStudent', methods = ['POST'])
def create_student():
    data = request.form
    studentID = data ['studentID']
    name = data ['name'] 
    dob = data ['dob']
    degree = data ['degree'] 
    reviews_received = data ['reviews_received'] 
    score = data ['score']
    student = add_student(studentID, name, dob, degree, reviews_received, score)

    if student:
        flash ('Student Added')
    flash ('Error in adding student')
    return redirect ('/')

@student_views.route('/searchStudent', methods = ['GET, ''POST'])
def search_for_student():
    data = request.form
    studentID = data ['studentID']

    student = search_student (username)
    if student:
        return render_template ('index.html', student = student)
    else:
        flash ('Student not Found')
        return redirect ('/')

@student_views.route('/listStudents', methods = ['GET'])
def list_students():
    students = get_all_students()

    return render_template ('index.html', students = students)

@student_views.route('/updateStudent', methods = ['GET', 'POST'])
def update_score():
    data = request.form
    studentID = data ['studentID']
    score = data ['score']
    student = add_student(studentID, score)

    if student:
        flash ('Student updating')
    flash ('Error in updating student')
    return redirect ('/')
