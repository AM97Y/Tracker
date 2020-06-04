from flask import render_template
from app import app
from app.DB.habits import Habits
from app.DB.persons import Persons

db = Habits()
@app.route('/')
def get_db_habits():
    return "HHHHHH"

@app.route('/add')
def add():
    db.add({"name": "Зарядка",
	 "start": "10.04.2020",
     "user": "admin",
	 "end": "14.04.2020",
	 "chek": "11.04.2020"
	})
    
@app.route('/login')
def login():
    pass

@app.route('/index') 
def index():
 return '''<div style="font-size:150pz">Test!</div>'''

