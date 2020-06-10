from flask import Flask
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
from flask_back.DB.habits import Habits
#import flask_back.DB.parser  
import os

app = Flask(__name__, static_url_path='/')
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = '/public'
CORS(app)


@app.route('/')
@cross_origin(origin='*')
def index():
    return ''' <div>Hello</div> '''

