from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Spencer'}
    return render_template('writetest.html', title='Home', user=user)