from flask_wtf import FlaskForm
#theres the field
from wtforms import StringField, PasswordField, SubmitField, BooleanField
#field cant be empty
from wtforms.validators import DataRequired, ValidationError
from aplicativo.models import User
#registration field
class RegistrationForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField ('confirm pass', validators=[DataRequired()])
    submit=SubmitField("Sign up")
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError (f'thats username already exist, pls choose another one')
#Login Field
class LoginForm (FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember= BooleanField("remember me")
    submit = SubmitField("Login")
