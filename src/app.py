from flask import Flask, request, render_template
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Load the dataset
total_data = pd.read_csv("../data/raw/House_Rent_Dataset.csv")

# Extract unique city names from the 'City' column
unique_cities = total_data['City'].unique()

# Load the preprocessor and model
preprocessor = joblib.load('preprocessor.pkl')
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_rent = None
    user_input = None

    if request.method == 'POST':
        city = request.form['city']
        size = float(request.form['size'])
        bathroom = int(request.form['bathroom'])
        
        # Create DataFrame from user input
        user_input = pd.DataFrame([[city, size, bathroom]], columns=['City', 'Size', 'Bathroom'])
        
        # Preprocess and predict
        processed_input = preprocessor.transform(user_input)
        predicted_rent = model.predict(processed_input)[0]

    return render_template('index.html', cities=unique_cities, predicted_rent=predicted_rent, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
