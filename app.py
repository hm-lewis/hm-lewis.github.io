# ~/app.py  —  Combined app for PythonAnywhere
# Place this file at /home/hmlewis/app.py
#
# URL layout:
#   hmlewis.eu.pythonanywhere.com/                → Landing page
#   hmlewis.eu.pythonanywhere.com/exam-generator  → Exam Generator
#   hmlewis.eu.pythonanywhere.com/chords          → Chord Practice App

import sys
import os

sys.path.insert(0, '/home/hmlewis/exam-generator')
sys.path.insert(0, '/home/hmlewis/chord-practice-app')

from flask import Flask, send_from_directory
from exam_blueprint import exam
from chord_blueprint import chord

app = Flask(__name__)

LANDING_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'landing')

@app.route('/')
def landing():
    return send_from_directory(LANDING_DIR, 'index.html')

@app.route('/styles.css')
def landing_css():
    return send_from_directory(LANDING_DIR, 'styles.css')

app.register_blueprint(exam, url_prefix='/exam-generator')
app.register_blueprint(chord, url_prefix='/chords')
