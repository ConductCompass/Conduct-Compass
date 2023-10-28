import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from App.main import create_app
from App.database import db, create_db
from App.models import User, Staff, Student, Review, Upvote, Downvote, KarmaScore
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user,
    create_staff,
    get_staff,
    get_all_staff_json,
    add_student,
    search_student,
    update_student,
    get_student,
    get_all_students_json,
    log_review,
    get_review,
    get_all_reviews_json,
    update_review_upvotes,
    update_review_downvotes,
    upvote_review,
    get_upvotes_json,
    downvote_review,
    get_downvotes_json,
    calculate_karma_score
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_staff(self):
        staff = Staff("bob", "bobpass")
        assert staff.username == "bob"
        assert staff.reviews_logged == 0

    # pure function no side effects or integrations called
    def test_get_json(self):
        staff = Staff("bob", "bobpass")
        staff_json = staff.get_json()
        self.assertDictEqual(staff_json, {"staffID":None, "staffName":"bob", "reviews_logged":0})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        staff = Staff("bob", password)
        assert staff.password != password

    def test_check_password(self):
        password = "mypass"
        staff = Staff("bob", password)
        assert staff.check_password(password)


class StudentUnitTests(unittest.TestCase):

    def test_new_student(self):
        student = Student(100, "rob", "2002-10-10T10:10:10", "IT")
        assert student.name == "rob"
        assert student.studentID == 100

    def test_get_json(self):
        student = Student(100, "rob", "2002-10-10T10:10:10", "IT")
        student_json = student.get_json()
        self.assertDictEqual(student_json, {"studentID": 100,
            "name": "rob",
            'dob': "2002-10-10T10:10:10",
            "degree": "IT",
            "reviews_received": 0,
            "score": 0})

class ReviewUnitTests(unittest.TestCase):

    def test_new_review(self):
        review = Review(20, 100, 200, "comment", 5, 2)
        assert review.reviewID == 20
        assert review.studentID == 100
        assert review.staffID == 200
        assert review.comments == "comment"
        assert review.upvotes == 5
        assert review.downvotes == 2

    def test_get_json(self):
        review = Review(20, 100, 200, "comment", 5, 2)
        review_json = review.get_json()
        self.assertDictEqual(review_json, {"reviewID":20, "studentID":100, 
                                          "staffID":200, "comments":"comment", 
                                          "upvotes":5, "downvotes":2})
        

class UpvoteUnitTests(unittest.TestCase):

    def test_new_upvote(self):
        upvote = Upvote(50, 200, 20)
        assert upvote.upvoteID == 50
        assert upvote.staffID == 200
        assert upvote.reviewID == 20

    def test_get_json(self):
        upvote = Upvote(50, 200, 20)
        upvote_json = upvote.get_json()
        self.assertDictEqual(upvote_json, {"upvoteID":50, "staffID":200, "reviewID":20})


class DownvoteUnitTests(unittest.TestCase):

    def test_new_downvote(self):
        downvote = Downvote(60, 200, 20)
        assert downvote.downvoteID == 60
        assert downvote.staffID == 200
        assert downvote.reviewID == 20

    def test_get_json(self):
        downvote = Downvote(60, 200, 20)
        downvote_json = downvote.get_json()
        self.assertDictEqual(downvote_json, {"downvoteID":60, "staffID":200, "reviewID":20})


class KarmaUnitTests(unittest.TestCase):
    
    def test_new_karma(self):
        karma = KarmaScore(50, 100, 0)
        assert karma.ID == 50
        assert karma.studentID == 100
        assert karma.score == 0
            
    def test_get_json(self):
        karma = KarmaScore(2, 100, 0)
        karma_json = karma.get_json()
        self.assertDictEqual(karma_json, {"ID":2, "studentID":100, "score":0})    
    
'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    staff = create_staff("bob", "bobpass")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_staff(self):
        staff = create_staff("rick", "bobpass")
        assert staff.username == "rick"

    def test_get_all_staff_json(self):
        staff_json = get_all_staff_json()
        self.assertListEqual([{"staffID":1, "staffName":"bob", "reviews_logged":0}, {"staffID":2, "staffName":"rick", "reviews_logged":0}], staff_json)

    

class StudentsIntegrationTests(unittest.TestCase):
    def test_add_student(self):
        student = add_student(100, "rob", "2002-10-10T10:10:10", "IT")
        assert student.name == "rob"

    def test_get_all_students_json(self):
        students_json = get_all_students_json()
        self.assertListEqual([{"studentID": 100,
            "name": "rob",
            'dob': datetime(2002,10,10,10,10,10),
            "degree": "IT",
            "reviews_received": 0,
            "score": 0}], students_json)

# Tests data changes in the database
    def test_update_student(self):
        student = get_student(100)
        assert student.name == "rob"
        assert student.score == 0

        update_student(100, 10)
        student = get_student(100)
        assert student.name == "rob"
        assert student.score == 10


class ReviewIntegrationTests(unittest.TestCase):
    def test_log_review(self):
        review = log_review(20, 100, 2, "comment", 5, 2)
        assert review.reviewID == 20 
        
    def test_get_all_reviews_json(self):
        review = log_review(30, 100, 2, "comment", 5, 2)
        reviews_json = get_all_reviews_json()
        self.assertListEqual([{"reviewID":30, "studentID":100, "staffID":2, "comments":"comment", "upvotes":5, "downvotes":2}], reviews_json)

    def test_update_upvotes(self):
        review = log_review(40, 100, 2, "comment", 0, 0)
        assert review.upvotes == 0
        update_review_upvotes(40)
        assert review.upvotes == 1

    def test_update_downvotes(self):
        review = log_review(50, 100, 2, "comment", 0, 0)
        assert review.downvotes == 0
        update_review_downvotes(50)
        assert review.downvotes == 1


class UpvoteIntegrationTests(unittest.TestCase):
    def test_upvote_review(self):
        upvote = upvote_review(50, 20, 1)
        assert upvote.upvoteID == 50
        
    def test_get_upvotes_json(self):
        upvote = upvote_review(60, 20, 2)
        upvotes_json = get_upvotes_json()
        self.assertListEqual([{"upvoteID":60, "reviewID":20, "staffID":2}], upvotes_json)


class DownvoteIntegrationTests(unittest.TestCase):
    def test_downvote_review(self):
        downvote = downvote_review(70, 20, 1)
        assert downvote.downvoteID == 70
        
    def test_get_downvotes_json(self):
        downvotes_json = get_downvotes_json()
        self.assertListEqual([{"downvoteID":70, "reviewID":20, "staffID":1}], downvotes_json)

class KarmaIntegrationTests(unittest.TestCase):
    def test_karma(self):
        score = calculate_karma_score(100)
        student = get_student(100)
        assert student.score == 6
        update_student(100, score)
        assert student.score == 6
        
