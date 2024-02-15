from flask import Flask
from flask.helpers import redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///diagno.db'
db = SQLAlchemy(app)

from diagno import routes
