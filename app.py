from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'la_cle_secrete'

debug = DebugToolbarExtension(app)

responses = []

# To-do: reset the following on completion of the survey
progress = 0

@app.route('/')
def show_survey_start():
    return render_template('base.html')

@app.route(f'/questions/{progress}')
def show_questions():
    # reply = request.form[progress]
    # responses.append(reply)
    # progress += 1
    print(progress)
    return redirect(f'/questions/1')