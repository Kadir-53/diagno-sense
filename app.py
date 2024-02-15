from flask import Flask
from flask.helpers import redirect
from flask.templating import render_template

from flask import Flask
app = Flask(__name__, static_url_path='/static')

app = Flask(__name__)


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
  return render_template('signup.html')


@app.route("/symptoms")
def symptoms():
  return render_template('symptoms.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
