from flask import Flask

# Create a Flask Instance
app = Flask(__name__)


def get_app():
    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
        app.config['SECRET_KEY'] = 'secret'
    return app
