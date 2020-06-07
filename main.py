from flask import Flask	
from datetime import datetime, timedelta

#UPLOAD_FOLDER = '/react_traker/public'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#def root():
#    return app.send_static_file("index.html")
@app.route('/')
@app.route('/index')

def main():
	now = datetime.utcnow() + timedelta(hours = 3)
	weekend = datetime.strptime('2020-06-14 23:59:59', '%Y-%m-%d %H:%M:%S')
	weekend_minutes_count = (weekend - now).days * 24 * 60 + int((weekend - now).seconds / 60)
	return '''
		<div style="font-size:150pz">До начала приема работы осталось {weekend_minutes_count} минут. Держимся!</div>
	'''.format(weekend_minutes_count=weekend_minutes_count)

