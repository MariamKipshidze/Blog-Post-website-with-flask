from flask import Flask

# Create a Flask Instance
app = Flask(__name__)


def get_app():
    with app.app_context():
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:1@localhost/my_new_database'
        app.config['SECRET_KEY'] = 'secret'
    return app
