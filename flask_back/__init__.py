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


@app.route('/api/v1.0/authorization')
@cross_origin(origin='*')
def authorization():
    return flask_back.DB.parser.get_person_data(request.args.get('login'),request.args.get('password')).to_json() 


@app.route('/add_person')
@cross_origin(origin='*')
def add_person(login, password):
    return flask_back.DB.parser.add_person(request.args.get('login'),request.args.get('password'))

@app.route('/add_person')
@cross_origin(origin='*')
def add_person_habit(login, password, name, start, end):
    return flask_back.DB.parser.add_person_habit(request.args.get('login'),request.args.get('password'),request.args.get('name'),request.args.get('start'), request.args.get('end'))

@app.route('/add_person')
@cross_origin(origin='*')
def add_check_for_persons_habit(login, password, name, start, end):
    return flask_back.DB.parser.add_check_for_person_habit(request.args.get('login'),request.args.get('password'),request.args.get('name'),request.args.get('start'), request.args.get('end'))
