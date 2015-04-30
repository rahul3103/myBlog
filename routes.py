from flask import Flask, url_for, request, render_template;
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

@app.route('/create',methods=['GET','POST'])
def create():
	if request.method == 'GET':
		# send the user the form
		return render_template('CreateQuestion.html');
	elif request.method == 'POST':
		# read from data and save it
		title = request.form['title'];
		answer = request.form['answer'];
		question = request.form['question'];
		
		# Store data in data base
		return render_template('CreatedQuestion.html', question = question);
	else:
		return "<h2>Invalid request</h2>";
	

@app.route('/question/<title>', methods=['GET','POST'])
def question (title):
	if request.method == 'GET':
		# send the user the form

		question = 'Question here';
		#Read question from data here
		return render_template('AnswerQuestion.html', question = question);
	elif request.method == 'POST':
		# User has attempted answer. Check if they are correct
		submittedAnswer = request.form['submittedAnswer'];
		
		# Read answer from data store
		answer = 'Answer';

		if submittedAnswer == answer:
			return  render_template(Correct.html);
		else:
			return render_template('Incorrect.html',submittedAnswer = submittedAnswer, answer = answer);
	else:
		return '<h2>Invalid request</h2>';