from flask import flask, render_template, request, redirect
from surveys import *

app = Flask(__name__)

responses = []

progress = 0

# @app.route('/')
# def show_survey_start():
#     return render_template('base.html')

# @app.route(f'/questions/{progress}')
# def show_questions():
#     progress += 1
#     return redirect(f'/questions/{progress}')