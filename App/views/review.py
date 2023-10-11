from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (log_review, get_all_reviews, get_all_reviews_json, update_review_upvotes, update_review_downvotes)
review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/logReview', methods = ['POST'])
def add_review():
    data = request.form
    reviewID = data ['reviewID']
    studentID = data ['studentID']
    staffID = data ['staffID']
    comments = data ['comments'] 
    upvotes = data ['upvotes']
    downvotes = data ['downvotes']

    review = log_review (reviewID, studentID, staffID, comments, upvotes, downvotes)

    if review:
        flash ('Review added')
        return render_template('index.html')
    flash ('Error in adding review')
    return render_template ('index.html')

@review_views.route('/reviewView', methods = ['GET'])
def view_review():
    reviews = get_all_reviews()

    return render_template ('index.html', reviews = reviews)

@review_views.route('/upReview', methods = ['POST'])
def upvote_review():
    data = request.form

    review = data ['reviewID']
    
    update_review_upvotes (review)

    return render_template ('index.html')


@review_views.route('/downReview', methods = ['POST'])
def downvote_review():
    data = request.form

    review = data ['reviewID']
    
    update_review_downvotes (review)

    return render_template ('index.html')
