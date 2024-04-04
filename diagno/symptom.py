import statistics
from flask import Flask, render_template, request, jsonify
import pickle

import numpy as np



# Load models and objects from saved pickle files
with open('final_rf_model.pkl', 'rb') as f:
    final_rf_model = pickle.load(f)

with open('final_nb_model.pkl', 'rb') as f:
    final_nb_model = pickle.load(f)

with open('final_svm_model.pkl', 'rb') as f:
    final_svm_model = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

with open('data_dict.pkl', 'rb') as f:
    data_dict = pickle.load(f)

def predictDisease(symptoms):
  symptoms = symptoms.split(",")

  # creating input data for the models
  input_data = [0] * len(data_dict["symptom_index"])
  for symptom in symptoms:
    index = data_dict["symptom_index"][symptom]
    input_data[index] = 1

  # reshaping the input data and converting it
  # into suitable format for model predictions
  input_data = np.array(input_data).reshape(1,-1)

  # generating individual outputs
  rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
  nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
  svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]

  # making final prediction by taking mode of all predictions
  final_prediction = statistics.mode([rf_prediction, nb_prediction, svm_prediction])
  predictions = {
    "rf_model_prediction": rf_prediction,
    "naive_bayes_prediction": nb_prediction,
    "svm_model_prediction": svm_prediction,
    "final_prediction":final_prediction
  }

  return final_prediction
