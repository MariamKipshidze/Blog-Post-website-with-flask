from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<int:user_id>')
def user(user_id):
    return f'<h1>User {user_id}</h1>'
