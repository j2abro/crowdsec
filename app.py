import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

# data structure to use for testing various page loading scenarios
mylist = ['one', 'two', 'three', 'four']

# categories for log.html (log an issue form), this will probably get moved elsewhere....
myCategories = [
	'Physical Security', 
	'Data Security', 
	'Web Application Security',
	'Network Security',
	'Theft',
	'Policy Issue',
	'Wireless Security',
	'Employee Safety',
	'Other']

# route to home page, the mylist data is not used on this page
@app.route('/')
@app.route('/index.html') 
def homepage():
	return render_template('index.html', listdata=mylist)

# log an issue form
@app.route('/log.html') 
def logissue():
	return render_template('log.html', listdata=myCategories)		

# default error 
@app.errorhandler(404)
def page_not_found(error): 
	return render_template('404.html'), 404

# IDEALIST: this is a page that is served and referenced from j2 blog, i'll find a new home for this later.
# for now, this page just requires this statement, the templates/idealist.html file and associated .js & .css files
@app.route('/idealist/') 
def idealist():
	return render_template('idealist.html', listdata=mylist)

#### TESTING (start) #####

# j2 page to mess around with flask/jinja, tablesorter
@app.route('/jtest/')
@app.route('/data/<mydata>')
def jtest(mydata=None):
	return render_template('jtest.html', mydata=mydata)

# from flaskr demo
@app.route('/user/<name>')
def show_name(name):
	return 'VERSION 2 - your name is %s' % name

#### TESTING (end) #####	


# debug not suitable for production
app.debug = True
if __name__ == '__main__':
	# bind to PORT if defined, otherwise default to 5000
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
