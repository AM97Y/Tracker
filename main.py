from flask import Flask, send_from_directory
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
from DB.habits import Habits
import os

app = Flask(__name__, static_folder='./public/', static_url_path='/')
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = '/public'
CORS(app)

@app.route('/')
@cross_origin(origin='*')
def index():
    return app.send_static_file('index.html')
