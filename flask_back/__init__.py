from flask import Flask
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
import flask_back.DB.parser  
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
@cross_origin(origin='*')
def index():
    hobbit_list = str(flask_back.DB.parser.get_data())
    return ''' <div>{hobbit_list}</div> '''.format(hobbit_list = hobbit_list)

#def get():
    #return flask_back.DB.parser.get_data()

