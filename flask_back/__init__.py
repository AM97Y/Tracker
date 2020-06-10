from flask import Flask
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
import flask_back.DB.parser  
import os

app = Flask(__name__, static_url_path='/')
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
@cross_origin(origin='*')
def index():
    return ''' <div>Hello</div> '''

def get():
    return flask_back.DB.parser.get_data()

