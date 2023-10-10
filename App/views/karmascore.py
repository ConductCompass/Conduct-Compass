from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (calculate_karma_score)

karmascore_views = Blueprint('karmascore_views', __name__, template_folder='../templates')

@karmascore_views.route('/karmascore', methods = ['GET'])
def karma_page():
    #score = calculate_karma_score()
    return render_template('index.html')
