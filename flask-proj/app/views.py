from flask import render_template
from app import app
from app.DB.habits import Habits
from app.DB.persons import Persons

db = Habits()
@app.route('/')
def get_db_habits():
    return ""

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
 import subprocess
 cmd = subprocess.Popen(['sudo', './ps_mem'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 out,error = cmd.communicate()
 memory = out.splitlines()
 return render_template('index.html', memory=memory)
