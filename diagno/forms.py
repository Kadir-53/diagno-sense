from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms import validators, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


class RegisterForm(FlaskForm):
  fname = StringField(label='First Name',
                      validators=[DataRequired(),
                                  Length(min=2, max=15)])
  lname = StringField(label='Last Name',
                      validators=[DataRequired(),
                                  Length(min=2, max=15)])
  age = IntegerField(label='Age',
                     validators=[
                         DataRequired(),
                         NumberRange(min=0,
                                     max=100,
                                     message="Age must be between 0 and 100")
                     ])
  gender = SelectField('Gender',
                       choices=[('Male', 'Male'), ('Female', 'Female'),
                                ('Others', 'Others')])
  email = StringField(label='Email', validators=[DataRequired(), Email()])
  password1 = PasswordField(label='Password',
                            validators=[DataRequired(),
                                        Length(min=6)])
  password2 = PasswordField(label='Confirm Password',
                            validators=[
                                DataRequired(),
                                EqualTo('password1',
                                        message='Passwords must match')
                            ])
  submit = SubmitField(label='Create Account')
