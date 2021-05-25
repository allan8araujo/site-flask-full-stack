from aplicativo import app
from flask import render_template,request,url_for


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
