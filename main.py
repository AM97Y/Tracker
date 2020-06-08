from flask import Flask, send_from_directory
from datetime import datetime, timedelta
from DB.habits import Habits
import os

app = Flask(__name__, static_folder='./react_tracker/public/', static_url_path='/')
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = './react_tracker/public'

@app.route('/')
def index():
    return app.send_static_file('index.html')
