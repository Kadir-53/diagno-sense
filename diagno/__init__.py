from flask import Flask
from flask.helpers import redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///diagno.db'
app.config['SECRET_KEY'] = 'mySecretKey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from diagno import routes
