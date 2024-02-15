from diagno import db


class Users(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
  fname = db.Column(db.String(length=20), nullable=False)
  lname = db.Column(db.String(length=20), nullable=False)
  age = db.Column(db.Integer(), nullable=False)
  gender = db.Column(db.String(length=20), nullable=False)
  email = db.Column(db.String(length=50), nullable=False, unique=True)
  password_hash = db.Column(db.String(length=60), nullable=False)


# u1 = Users(fname='Harry', lname='Foe', age=20, gender='Male', email='john@gmail.com', password_hash='123456')


class Item(db.Model):
  __tablename__ = "items"
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  price = db.Column(db.Integer(), nullable=False)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  description = db.Column(db.String(length=1024), nullable=False, unique=True)

  def __repr__(self):
    return f'Item {self.name}'
