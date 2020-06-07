from flask import Flask	
from datetime import datetime, timedelta

app = Flask(__name__, static_folder='./react_tracker/public', static_url_path='/')
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = 'react_tracker/public'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/loadfile/<filename>')
def uploaded_file(filename):
    image = send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return image