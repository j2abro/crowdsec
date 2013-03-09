import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

# data structure to use for testing various page loading scenarios
mylist = ['one', 'two', 'three', 'four']

# route to home page, the mylist data is not used on this page
@app.route('/')
@app.route('/index.html') 
def homepage():
	return render_template('index.html', listdata=mylist)

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

# log an issue form
@app.route('/log.html') 
def logissue():
	return render_template('log.html', listdata=myCategories)


# data structure used to populate report form. This is an array of tuples, but could be whatever.
report_table = [
	(	"Fred", "03-11-2013", "Physical Security", "I noticed that the back door that leads to the back parking lot often is unlocked." ), 
	(	"Anonymous", "03-08-2013", "Web Application Security", "Due to deadlines and lack of awareness among the dev team, we consistently push out releases that have not been tested for input validation. I am worried that we may be vulnerable to SQL injection." ), 
	(	"sue", "03-08-2013", "Wireless Security", "Sometimes when I see the network list in my iPhone, other wireless networks appear. Potential rogue wifi APs on the netword?" ), 
	(	"bob", "03-06-2013", "Data Security", "I frequently see company laptops during offsite events. I am not sure how those are configured, but mine does not have full disk encryption. As most emlpoyees have some sort of customer data on their laptions, this is likely a security risk." ),
	(	"Bill", "03-06-2013", "Physical Security", "I routinely tailgate through the front door without my badge." ),
	(	"Anonymous", "03-04-2013", "Network Security", "I think we have a couple of servers hosted on the internal network that have direct internet connections." ),
	(	"bob", "03-01-2013", "Physical Security", "The guard often does not have guests sign in at front desk." )
]

# log an issue form
@app.route('/reports.html') 
def reports():
	return render_template('reports.html', report_table = report_table)

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
