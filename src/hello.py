# hello.py
from flask import Flask, jsonify, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model from a file
model = pickle.load(open('decision_tree_classifier_default_42.sav', 'rb'))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json(force=True)
    
    # Convert JSON data to DataFrame
    prediction_data = pd.DataFrame(data, index=[0])
    
    # Make prediction using the loaded model
    prediction = model.predict(prediction_data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
