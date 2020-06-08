from flask import Flask	
from datetime import datetime, timedelta
from DB.habits import Habits

app = Flask(__name__, static_folder='./react_tracker/public/', static_url_path='/')
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = 'react_tracker/public'

@app.route('/')
def index():
    db = Habits()
    print(db.get_all())
    return app.send_static_file('index.html')

@app.route('/favicon.ico')
def favicon():
    print(str(send_from_directory(os.path.join(app.root_path, './react_tracker/puplic/'),'favicon.ico')))
    return send_from_directory(os.path.join(app.root_path, './react_tracker/puplic/'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

