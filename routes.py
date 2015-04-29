from flask import Flask, url_for;
from app import app;

@app.route('/')
def hello():
	createLink = "<a href = '" + url_for('create') + "'>Create a question</a>";
	return """<html>
				<head>
				  <title>Hello World!</title>
				</head>
				<body>
				  """+ createLink +"""
				</body>
			  </html>""";

@app.route('/create')
def create():
	return "<h2>This is the create page!</h2>";


@app.route('/question/<title>')
def question (title):
	return'<h2>' + title +' </h2>';