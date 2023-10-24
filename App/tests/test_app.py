import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Staff, Student, Review, KarmaScore
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_staff(self):
        staff = Staff("bob", "bobpass", 5)
        assert staff.username == "bob"
        assert staff.reviews_logged == 5

    # pure function no side effects or integrations called
    def test_get_json(self):
        staff = Staff("bob", "bobpass", 5)
        staff_json = staff.get_json()
        self.assertDictEqual(staff_json, {"staffID":None, "staffName":"bob", "reviews_logged":5})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        staff = Staff("bob", password, 5)
        assert staff.password != password

    def test_check_password(self):
        password = "mypass"
        staff = Staff("bob", password, 5)
        assert staff.check_password(password)


class StudentUnitTests(unittest.TestCase):

    def test_new_student(self):
        student = Student(100, "rob", "2002-10-10T10:10:10", "IT", 0, 0)
        assert student.name == "rob"
        assert student.studentID == 100

    def test_get_json(self):
        student = Student(100, "rob", "2002-10-10T10:10:10", "IT", 0, 0)
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


class KarmaUnitTests(unittest.TestCase):
    
    def test_new_karma(self):
        karma = KarmaScore(2, 100, 0)
        assert karma.ID == 2
        assert karma.studentID == 100
        assert karma.score == 0
            
    def test_get_json(self):
        karma = KarmaScore(2, 100, 0)
        karma_json = karma.get_json()
        self.assertDictEqual(karma_json, {"ID":2, "studentID":100, "score":0})    
    

'''
    Integration Tests


# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
'''