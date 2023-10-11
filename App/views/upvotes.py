from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (upvote_review, get_upvotes)

upvote_views = Blueprint('upvote_views', __name__, template_folder='../templates')

@upvote_views.route('/upvote', methods = ['POST'])
def upvote():
    data = request.form
    upvoteID = data ['upvoteID']
    reviewID = data ['reviewID']
    staffID  = data ['staffID']

    upvote_review (upvoteID, reviewID, staffID) 

    return render_template ('/')

@upvote_views.route('/listUpvote', methods = ['POST'])
def listUpvote():
    upvotes = get_upvotes()

    return render_templaet ('index.html', upvotes = upvotes)
