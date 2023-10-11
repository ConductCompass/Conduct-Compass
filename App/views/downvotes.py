from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (downvote_review, get_downvotes)

downvote_views = Blueprint('downvote_views', __name__, template_folder='../templates')

@downvote_views.route('/downvote', methods = ['POST'])
def downvote():
    data = request.form
    downvoteID = data ['downvoteID']
    reviewID = data ['reviewID']
    staffID  = data ['staffID']

    downvote_review (downvoteID, reviewID, staffID) 

    return render_template ('/')

@downvote_views.route('/listdownvote', methods = ['POST'])
def listDownvote():
    downvotes = get_downvotes()

    return render_template ('index.html', downvotes = downvotes)
