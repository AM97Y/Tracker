from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
import flask_back.DB.parser  
from bson.json_util import loads, dumps
from bson.raw_bson import RawBSONDocument
import bsonjs

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
def index():
    return '''<div>Hey</div>'''


@app.route('/authorization')
@cross_origin(origin='*')
def authorization(): 
    return jsonify(str(flask_back.DB.parser.get_person_id(request.args.get('login'),request.args.get('password'))))

@app.route('/get_person_data')
@cross_origin(origin='*')
def get_data(): 
    habits = (flask_back.DB.parser.get_person_data(request.args.get('_id')))[0]
    print(habits)
    json_record2 = bsonjs.dumps(habits)
    print(json_record2)
    return json_record2
    #return jsonify({'results': habs})
    #jsonify({'data': flask_back.DB.parser.get_person_data(request.args.get('_id'))[0]})

@app.route('/add_person')
@cross_origin(origin='*')
def add_person():
    return jsonify(str(flask_back.DB.parser.add_person(request.args.get('login'),request.args.get('password'))))

@app.route('/add_person_habit')
@cross_origin(origin='*')
def add_person_habit():
    return jsonify(str(flask_back.DB.parser.add_person_habit(request.args.get('_id'),request.args.get('name'),request.args.get('start'), request.args.get('end'))))

@app.route('/add_check_for_person_habit')
@cross_origin(origin='*')
def add_check_for_persons_habit():
    return jsonify(str(flask_back.DB.parser.add_check_for_person_habit(request.args.get('_id'),request.args.get('name'),request.args.get('start'), request.args.get('end'))))
