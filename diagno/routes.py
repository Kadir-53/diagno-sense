from flask import render_template, redirect, url_for, request, jsonify, flash
from diagno import app, db
from diagno.models import Item, Users
from diagno.forms import RegisterForm, LoginForm
from diagno.symptom import predictDisease
from flask_login import login_user, logout_user, login_required
import os
import pickle
import pandas as pd


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
                           password=form.password1.data)
    db.session.add(user_to_create)
    db.session.commit()
    return redirect(url_for('login'))
  if form.errors != {}:
    for msg in form.errors.values():
      flash(f'There was an error with creating the user: {msg}',
            category='danger')
  return render_template('signup.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    attempted_user = Users.query.filter_by(email=form.email.data).first()
    if attempted_user and attempted_user.check_password(
        attempted_password=form.password.data):
      login_user(attempted_user)
      flash(f'You are now logged in as {attempted_user.fname}',
            category='success')
      return redirect(url_for('index'))

    else:
      flash('Login unsuccessful. Please check email and password',
            category='danger')

  return render_template('login.html', form=form)


@app.route("/logout")
def logout():
  logout_user()
  flash('You have been logged out', category='info')
  return redirect(url_for('index'))


@app.route("/symptoms")
@login_required
def symptoms():
  return render_template('symptoms.html')


@app.route('/predict', methods=['POST'])
def predict():
  symptoms = request.form['symptoms']
  final_prediction = predictDisease(symptoms)
  return jsonify({'final_prediction': final_prediction})


@app.route("/market")
def market():
  items = Item.query.all()
  return render_template('market.html', items=items)


dataset_dir = os.path.join(os.path.dirname(__file__), 'dataset')
model_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.sav')
diabetes_model = pickle.load(open(model_path, 'rb'))


@app.route('/diabetes_prediction', methods=['GET', 'POST'])
def diabetes_prediction():
  if request.method == 'GET':
    return render_template('diabetes_prediction.html')
  elif request.method == 'POST':
    # Get input data from the form
    pregnancies = float(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    blood_pressure = float(request.form['blood_pressure'])
    skin_thickness = float(request.form['skin_thickness'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetes_pedigree_function = float(
        request.form['diabetes_pedigree_function'])
    age = float(request.form['age'])

    # Perform prediction
    user_input = [
        pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
        diabetes_pedigree_function, age
    ]
    diab_prediction = diabetes_model.predict([user_input])

    # Return prediction result
    if diab_prediction[0] == 1:
      prediction_result = 'The person is diabetic'
    else:
      prediction_result = 'The person is not diabetic'

    return jsonify({"prediction_result": prediction_result})


@app.route('/diabetes_prediction_form')
def diabetes_prediction_form():
  return render_template('diabetes_prediction_form.html')


# Load the diabetes model
model_path = os.path.join(os.path.dirname(__file__), 'heart_disease_model.sav')
heart_disease_model = pickle.load(open(model_path, 'rb'))


@app.route("/heart_disease")
def heart_disease():
  return render_template('heart_disease.html')


@app.route('/heart_disease_prediction', methods=['POST'])
def predict_heart_disease():
  # Retrieve form data
  age = float(request.form['age'])
  sex = float(request.form['sex'])
  cp = float(request.form['cp'])
  trestbps = float(request.form['trestbps'])
  chol = float(request.form['chol'])
  fbs = float(request.form['fbs'])
  restecg = float(request.form['restecg'])
  thalach = float(request.form['thalach'])
  exang = float(request.form['exang'])
  oldpeak = float(request.form['oldpeak'])
  slope = float(request.form['slope'])
  ca = float(request.form['ca'])
  thal = float(request.form['thal'])

  # Perform prediction using the loaded model
  predicted_result = heart_disease_model.predict([[
      age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,
      slope, ca, thal
  ]])

  prediction_message = ""
  if predicted_result[0] == 1:
    prediction_message = 'The person is having heart disease'
  else:
    prediction_message = 'The person does not have any heart disease'

  # Return the prediction result as a JSON object
  return jsonify({"prediction_result": prediction_message})
