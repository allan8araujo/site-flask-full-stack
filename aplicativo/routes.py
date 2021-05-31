from aplicativo import app,db,bcrypt
from flask import render_template,request,url_for, flash, redirect
from aplicativo.forms import RegistrationForm, LoginForm
from aplicativo.models import User
from flask_login import login_user, current_user, logout_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login',methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(' please check unsername and password')
    return render_template('login.html',form=form)


@app.route('/register', methods=['POST','GET','PUT'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Sua conta {form.username.data} foi criada com sucesso!')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
