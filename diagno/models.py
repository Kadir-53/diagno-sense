from diagno import db, bcrypt, login_manager
from flask_login import UserMixin
from datetime import datetime, timezone


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


class SymptomPrediction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  symptoms = db.Column(db.String(255), nullable=False)
  predicted_disease = db.Column(db.String(255), nullable=False)
  date_time = db.Column(db.DateTime,
                        nullable=False,
                        default=datetime.now(timezone.utc))

  def __repr__(self):
    return f"SymptomPrediction(user_id={self.user_id}, symptoms='{self.symptoms}', predicted_disease='{self.predicted_disease}', date_time={self.date_time})"


class HeartDiseasePrediction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  name = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  sex = db.Column(db.Integer, nullable=False)
  trestbps = db.Column(db.Integer, nullable=False)
  chol = db.Column(db.Integer, nullable=False)
  fbs = db.Column(db.Integer, nullable=False)
  restecg = db.Column(db.Integer, nullable=False)
  thalach = db.Column(db.Integer, nullable=False)
  exang = db.Column(db.Integer, nullable=False)
  oldpeak = db.Column(db.Float, nullable=False)
  slope = db.Column(db.Float, nullable=False)
  ca = db.Column(db.Integer, nullable=False)
  thal = db.Column(db.Integer, nullable=False)
  cp = db.Column(db.Integer, nullable=False)
  predicted_result = db.Column(db.Integer,
                               nullable=False)  # Changed to Integer type
  date_time = db.Column(db.DateTime,
                        nullable=False,
                        default=datetime.now(timezone.utc))

  user = db.relationship('Users',
                         backref=db.backref('heart_disease_predictions',
                                            lazy=True))

  def __repr__(self):
    return f"HeartDiseasePrediction(id={self.id}, user_id={self.user_id}, name='{self.name}', age={self.age}, sex={self.sex}, trestbps={self.trestbps}, chol={self.chol}, fbs={self.fbs}, restecg={self.restecg}, thalach={self.thalach}, exang={self.exang}, oldpeak={self.oldpeak}, slope={self.slope}, ca={self.ca}, thal={self.thal}, cp={self.cp}, predicted_result={self.predicted_result}, date_time={self.date_time})"


class DiabetesPrediction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  name = db.Column(db.String(100), nullable=False)
  pregnancies = db.Column(db.Float, nullable=False)
  glucose = db.Column(db.Float, nullable=False)
  blood_pressure = db.Column(db.Float, nullable=False)
  skin_thickness = db.Column(db.Float, nullable=False)
  insulin = db.Column(db.Float, nullable=False)
  bmi = db.Column(db.Float, nullable=False)
  diabetes_pedigree_function = db.Column(db.Float, nullable=False)
  age = db.Column(db.Float, nullable=False)
  predicted_result = db.Column(db.Integer, nullable=False)  # 0 or 1
  date_time = db.Column(db.DateTime,
                        nullable=False,
                        default=datetime.now(timezone.utc))

  user = db.relationship('Users',
                         backref=db.backref('diabetes_predictions', lazy=True))

  def __repr__(self):
    return f"DiabetesPrediction(id={self.id}, user_id={self.user_id}, name='{self.name}', pregnancies={self.pregnancies}, glucose={self.glucose}, blood_pressure={self.blood_pressure}, skin_thickness={self.skin_thickness}, insulin={self.insulin}, bmi={self.bmi}, diabetes_pedigree_function={self.diabetes_pedigree_function}, age={self.age}, predicted_result={self.predicted_result}, date_time={self.date_time})"
