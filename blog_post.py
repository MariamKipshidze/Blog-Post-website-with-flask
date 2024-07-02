from flask import Flask, render_template, request

# Create a Flask Instance
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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


# Create custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
