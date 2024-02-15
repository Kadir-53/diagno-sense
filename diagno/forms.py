from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 


class RegisterForm(FlaskForm):
  fname = StringField(label='First Name')
  lname = StringField(label='Last Name')
  age = StringField(label='Age')
  gender = StringField(label='Gender')
  email = StringField(label='Email')
  password1 = PasswordField(label='Password')
  password2 = PasswordField(label='Confirm Password')