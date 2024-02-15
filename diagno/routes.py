from diagno import app
from flask import render_template
from diagno.models import Item


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/contact")
def contact():
  return render_template('contact.html')


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/signup")
def signup():
  if request.method == 'POST':
    fname = request.form.get['fname']
    fname = request.form.get['fname']
    fname = request.form.get['fname']
  return render_template('signup.html')


@app.route("/symptoms")
def symptoms():
  return render_template('symptoms.html')


@app.route("/market")
def market():
  items = Item.query.all()
  return render_template('market.html', items=items)
