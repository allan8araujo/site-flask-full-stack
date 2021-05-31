from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY'] = '715dd72b3f305604c95d88a129e3b23c'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

login_manager=LoginManager(app)
db= SQLAlchemy(app)
bcrypt= Bcrypt(app)

from aplicativo import routes