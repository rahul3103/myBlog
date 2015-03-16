from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('user_agent')
	return '<h1>Your Browser is %s</h1>'%user_agent

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' %name

if __name__ =='__main__':
	app.run(debug=True)