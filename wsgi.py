import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.models import Review, Staff

from App.database import db, get_migrate
from App.main import create_app
from App.controllers.user import ( create_user, get_all_users_json, get_all_users )
from App.controllers.staff import (create_staff, get_all_staff, get_all_staff_json)
from App.controllers.student import ( add_student, get_all_students_json, get_all_students, search_student, update_student )
from App.controllers.review import (log_review, get_all_reviews, get_all_reviews_json, update_review_upvotes, update_review_downvotes)
from App.controllers.upvote import (upvote_review, get_upvotes)
from App.controllers.downvote import (downvote_review, get_downvotes)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_staff('bobb', 'bobbpass')
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


'''Staff Commands  
'''
staff_cli = AppGroup('staff', help='Staff object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@staff_cli.command("create", help="Creates staff member")
@click.argument("username", default="robin")
@click.argument("password", default="robpass")
@click.argument("reviews_logged", default=0)
def create_staff_command(username, password):
    create_staff(username, password)
    print(f'Staff {username} created!')

# this command will be : flask user create bob bobpass

@staff_cli.command("list", help="Lists staff in the database")
@click.argument("format", default="string")
def list_staff_command(format):
    if format == 'string':
        print(get_all_staff())
    else:
        print(get_all_staff_json())

app.cli.add_command(staff_cli) # add the group to the cli



''' 
Student Commands
'''
student_cli = AppGroup('student', help='Student object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@student_cli.command("add", help="Creates a student")
@click.argument("id", default=1000)
@click.argument("name", default="studentname")
@click.argument("dob", default="2010-10-10T10:10:10")
@click.argument("degree", default="IT")

def add_student_command(id, name, dob, degree):
    student = add_student(id, name, dob, degree)
    if student:
        print(f'Student {id} - {name} added!')

@student_cli.command("list", help="Lists students in the database")
@click.argument("format", default="string")
def list_student_command(format):
    if format == 'string':
        print(get_all_students())
    else:
        print(get_all_students_json())

@student_cli.command("search", help="Search student in the database")
@click.argument("id")
def search_student_command(id):
    print(search_student(id))

@student_cli.command("update", help="Update student in the database")
@click.argument("id")
@click.argument("score")
def update_student_command(id, score):
    update_student(id, score)
    print(f'Student {id} updated!')

app.cli.add_command(student_cli) # add the group to the cli


'''
Review Commands
'''
review_cli = AppGroup('review', help='Review object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@review_cli.command("log", help="Logs a review")
@click.argument("id", default=4000)
@click.argument("studentid", default=1000)
@click.argument("staffid", default=2)
@click.argument("comments", default="staffcomment")
@click.argument("upvotes", default=0)
@click.argument("downvotes", default=0)

def log_review_command(id, studentid, staffid, comments, upvotes, downvotes):
    if log_review(id, studentid, staffid, comments, upvotes, downvotes):
        print(f'Review {id} has been logged!')

@review_cli.command("list", help="Lists reviews in the database")
@click.argument("format", default="string")
def list_reviews_command(format):
    if format == 'string':
        print(get_all_reviews())
    else:
        print(get_all_reviews_json())

app.cli.add_command(review_cli) # add the group to the cli


''' 
Upvote Commands
'''
upvote_cli = AppGroup('upvote', help='Upvote object commands') 

@upvote_cli.command("upvote_review", help="Upvote a review")
@click.argument("upvoteid", default=4000)
@click.argument("reviewid", default=2000)
@click.argument("staffid", default=5000)

def upvote_review_command(upvoteid, reviewid, staffid):
    review = Review.query.filter_by(reviewID=reviewid).first()
    staff = Staff.query.filter_by(staffID=staffid).first()
    if review and staff:
        upvote_review(upvoteid, reviewid, staffid)
        update_review_upvotes(reviewid)
        print(f'Review {reviewid} has been upvoted!')
    else:
        print(f'Review {reviewid} could not be upvoted')

@upvote_cli.command("list", help="Lists upvotes in the database")
@click.argument("format", default="string")
def get_upvotes_command(format):
    if format == 'string':
        print(get_upvotes())

app.cli.add_command(upvote_cli)


''' 
Downvote Commands
'''
downvote_cli = AppGroup('downvote', help='Downvote object commands') 

@downvote_cli.command("downvote_review", help="Downvote a review")
@click.argument("downvoteid", default=4000)
@click.argument("reviewid", default=2000)
@click.argument("staffid", default=5000)

def downvote_review_command(downvoteid, reviewid, staffid):
    review = Review.query.filter_by(reviewID=reviewid).first()
    staff = Staff.query.filter_by(staffID=staffid).first()
    if review and staff:
        downvote_review(downvoteid, reviewid, staffid)
        update_review_downvotes(reviewid)
        print(f'Review {reviewid} has been downvoted!')
    else:
        print(f'Review {reviewid} could not be downvoted')

@downvote_cli.command("list", help="Lists downvotes in the database")
@click.argument("format", default="string")
def get_downvotes_command(format):
    if format == 'string':
        print(get_downvotes())

app.cli.add_command(downvote_cli)


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)