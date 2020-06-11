from flask import Flask
from flask import request
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
import flask_back.DB.parser  
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
def index():
    return '''<div>Hey</div>'''


@app.route('/authorization')
@cross_origin(origin='*')

def authorization():
    user = flask_back.DB.parser.get_person_data()
    return '''
		<div style="font-size:150pz">User: {user}</div>
	'''.format(user=user)

'''
@app.route('/add_person/<login>/<password>')
@cross_origin(origin='*')
def add_person(login, password):
    return flask_back.DB.parser.add_person(login=login, password=password)

@app.route('/add_person/<login>/<password>/<name>/<start/<end>')
@cross_origin(origin='*')
def add_person_habit(login, password, name, start, end):
    return flask_back.DB.parser.add_person_habit(login=login, password=password, name=name, start=start, end=end)

@app.route('/add_person/<login>/<password>/<name>/<start/<end>')
@cross_origin(origin='*')
def add_check_for_persons_habit(login, password, name, start, end):
    return flask_back.DB.parser.add_check_for_person_habit(login=login, password=password, name=name, start=start, end=end)
'''