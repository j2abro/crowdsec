import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello world'

@app.route('/data/')
@app.route('/data/<mydata>')
def data(mydata=None):
	return render_template('data.html', mydata=mydata)

@app.route('/user/<name>')
def show_name(name):
	return 'VERSION 2 - your name is %s' % name
			
app.debug = True
if __name__ == '__main__':
	# bind to PORT if defined, otherwise default to 5000
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
