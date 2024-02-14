from flask import Flask, render_template, request, jsonify
import pickle

# Load the trained model and other necessary objects
with open('final_rf_model.pkl', 'rb') as f:
  final_rf_model = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
  encoder = pickle.load(f)

with open('data_dict.pkl', 'rb') as f:
  data_dict = pickle.load(f)

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('symptoms.html')


@app.route('/predict', methods=['POST'])
def predict():
  symptoms = request.form['symptoms']
  predictions = predictDisease(symptoms)
  return jsonify(predictions)


def predictDisease(symptoms):
  # Convert symptoms string to input data format
  input_data = [0] * len(data_dict["symptom_index"])
  for symptom in symptoms.split(","):
    index = data_dict["symptom_index"].get(symptom.strip().capitalize(), -1)
    if index != -1:
      input_data[index] = 1

  input_data = [input_data]  # Convert to 2D array
  final_prediction = final_rf_model.predict(input_data)
  final_prediction = encoder.inverse_transform(final_prediction)[0]

  return {"final_prediction": final_prediction}


if __name__ == '__main__':
  app.run(debug=True)
