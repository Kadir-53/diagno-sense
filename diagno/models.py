from diagno import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
  id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
  fname = db.Column(db.String(100), nullable=False)
  lname = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer(), nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)

  def __init__(self, fname, lname, age, gender, email, password):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender
    self.email = email
    self.password = password

  @property
  def password(self):
    return self.password

  @password.setter
  def password(self, plain_password):
    self.password_hash = bcrypt.generate_password_hash(plain_password).decode(
        'utf-8')

  def check_password(self, attempted_password):
    return bcrypt.check_password_hash(self.password_hash, attempted_password)


# u2 = Users(fname='Harry', lname='Foe', age=26, gender='Male', email='harry@gmail.com', password_hash='12345678')


class Item(db.Model):
  __tablename__ = "items"
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  price = db.Column(db.Integer(), nullable=False)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  description = db.Column(db.String(length=1024), nullable=False, unique=True)

  def __repr__(self):
    return f'Item {self.name}'
