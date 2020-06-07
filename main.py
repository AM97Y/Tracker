from flask import Flask	
from datetime import datetime, timedelta

#UPLOAD_FOLDER = '/react_traker/public'

#app = Flask(__name__)
app = Flask(__name__, static_folder='./react_tracker/public', static_url_path='/')
app.config['JSON_AS_ASCII'] = False
#app.config['UPLOAD_FOLDER'] = 'react_tracker/public'

#def root():
#    return app.send_static_file("index.html")
@app.route('/')
#@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/react_tracker/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'react_tracker', 'public'),
                               'favicon.ico', mimetype='image/png')