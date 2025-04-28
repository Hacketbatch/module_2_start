from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/newby')
def newby():
    return render_template('newPage.html')

@app.route('/contact')
def contact():
    return render_template('Contact us.html')

