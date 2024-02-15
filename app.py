from flask import Flask
from flask.helpers import redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///diagno.db'
db = SQLAlchemy(app)


class Item(db.Model):
  __tablename__ = "items"
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  price = db.Column(db.Integer(), nullable=False)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  description = db.Column(db.String(length=1024), nullable=False, unique=True)

  def __repr__(self):
    return f' Item{self.name}'


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


@app.route("/market")
def market():
  items = Item.query.all()
  return render_template('market.html', items=items)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
