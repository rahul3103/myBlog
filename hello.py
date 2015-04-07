from flask import Flask, render_template
from flask import request
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)

#@app.route('/')
#def index():
#	user_agent = request.headers.get('user_agent')
#	return '<h1>Your Browser is %s</h1>'%user_agent

@app.route('/user/<username>')
def user(username):
	return 'User %s!' %username

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

with app.test_request_context():
	print url_for('index')
	print url_for('login')
	print url_for('login', next='/')
	print url_for('profile', username='John Doe')

if __name__ =='__main__':
	app.run(debug=True)