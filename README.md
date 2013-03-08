# crowdsec

An experiment in crowdsourcing security risk management within an organization.

## Initial environment configuration

This is based on the python/flask example from heroku

	$ mkdir crowdsec
	$ cd crowdsec

Create a virtual environment in the 'venv' (directory will be created)

	$ virtualenv venv

Start the environment. your prompt will change: (venv)

	$ . venv/bin/activate

install/activate Flask in virtual environment

	$ pip install Flask

### Heroku specifics

requirements.txt: create a file in root app dir with following:
	
	Flask==0.9

Procfile: create a file named Procfile with the following text. Heroku uses to know how to launch app.
	web: python app.py

### GIT

Create .gitgnore file in root app directory with these excludes:
	$ venv
	$ *.pyc

Add/commit files

	git init
	git add .
	git commit -m "initial commit..."


### Heroku

Login with Heroku account

	$ heroku login
	
Test the app locally

	$ foreman start

Run on heroku (while logged into heroku)

	$ heroku create
	$ git push heroku master

This sets heroku to a single (free) instance
	$ heroku ps:scale web=1

Confirm it's running as defined, and view logs
	$ heroku ps
	$ heroku logs

## To update app

To edit app locally update heroku

To change a file:

	$ git -am 'changed home page'

Or to add a file

	$ git add mynewfile

To list files in git:

	$ git log --pretty=format: --name-only --diff-filter=A | sort -

Then commit changes and push to heroku

	$ git commit -am 'here is my comment'
	$ git push heroku


### To start new virtual env session

Go to dev directory and start virtualenv

	$ cd crowdsec
	
Then I've been doing this (but does this overwrite previous pip installs?, without doing this, i get an error on foreman start)	

	$ virtualenv venv

Start environment

	$ . venv/bin/activate

Then either start app locally

	$ foreman start

Or on live heroku platform

	$ git push heroku

