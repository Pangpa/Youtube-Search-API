import os, operator, flask
from flask import flash, render_template, request, redirect
from wtforms import Form, TextField, StringField, SelectField, TextAreaField, validators, SubmitField
from search import youtube_search
from googleapiclient.errors import HttpError
import json

app = flask.Flask('__name__')
app.secret_key = os.urandom(24)

class SearchForm(Form):
	name = TextField('Name:', validators=[validators.required()])
	search = StringField('') #

@app.route('/',methods=['GET', 'POST'])
def index():
	search = SearchForm(request.form)
	print(search.errors) #
	results = {} 
	if request.method == 'POST':
		#d= {'a':1,'b':2,'f':4}
		
		try:
			search_term = request.form['url']
			results = youtube_search(search_term)
		except HttpError as e:
			print ('An HTTP error %d occurred:\n%s' , e.resp.status, e.content)
			return render_template('index.html', results = {"response status": e.resp.status, "content": e.content})	
		#results = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
		#print("results = {}".format(results))
		#print(d.items())
		#return search_results(search)
		return render_template('index.html', results = results,data = json.dumps(results))
	return render_template('index.html', form = search)# search is obj of SearchForm()
"""
@app.route('/results')
def search_results(search):
	results = [] 
	search_string = search.data['search']
	print("in results")
"""
if __name__ == '__main__':
	app.run('localhost', 8090, debug = True)
