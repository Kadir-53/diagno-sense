from flask.helpers import flash
from diagno import app
from flask import render_template, redirect, url_for
from diagno.models import Item, Users
from diagno.forms import RegisterForm
from diagno import db


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/contact")
def contact():
  return render_template('contact.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
  form = RegisterForm()
  if form.validate_on_submit():
    user_to_create = Users(fname=form.fname.data,
                           lname=form.lname.data,
                           age=form.age.data,
                           gender=form.gender.data,
                           email=form.email.data,
                           password_hash=form.password1.data)
    db.session.add(user_to_create)
    db.session.commit()
    return redirect(url_for('login'))
  if form.errors != {}:
    for msg in form.errors.values():
      flash(f'There was an error with creating the user: {msg}',
            category='danger')

  return render_template('signup.html', form=form)


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/symptoms")
def symptoms():
  return render_template('symptoms.html')


@app.route("/market")
def market():
  items = Item.query.all()
  return render_template('market.html', items=items)
