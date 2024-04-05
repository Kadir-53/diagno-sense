from flask import Flask
from flask.helpers import redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import datetime
from pytz import timezone

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///diagno.db'
app.config['SECRET_KEY'] = 'mySecretKey'
app.config['TIMEZONE'] = 'Asia/Kolkata'  # Set the timezone to IST
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

ist_timezone = timezone('Asia/Kolkata')

from diagno import routes
