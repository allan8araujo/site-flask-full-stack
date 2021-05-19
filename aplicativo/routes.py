from aplicativo import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calc')
def calc():
    return render_template('calc.html')

@app.route('/about')
def about():
    return render_template('about.html')
