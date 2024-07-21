from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import EmailForm, UserForm

# Create a Flask Instance
app = Flask(__name__)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SECRET_KEY'] = 'secret'
# Initialize the database
db = SQLAlchemy(app)


# Create Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        # Process form data here
        username = form.username.data
        email = form.email.data

        # Create a new user
        new_user = User(name=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('add_user.html', form=form)


@app.route('/user/<int:user_id>')
def user(user_id):
    return render_template('user.html', user_id=user_id)


@app.route('/subscribe', methods=['GET'])
def subscribe():
    title = 'Subscribe to my blog post'
    return render_template('subscribe.html', title=title)


@app.route('/processing_subscription', methods=['POST'])
def processing_subscription():
    email = request.form['email']
    title = 'Thank you for subscribing to my blog post'
    return render_template('processing_subscription.html', title=title)


@app.route('/processing_subscription_with_wtf', methods=['GET', 'POST'])
def processing_subscription_with_wtf():
    email = None
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
        flash("Submitted successfully")

    return render_template(
        'processing_subscription_with_wtf.html',
        form=form,
        email=email
    )


# Create custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/success')
def success():
    return render_template('success.html'), 200
