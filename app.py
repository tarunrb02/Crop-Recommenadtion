from flask import Flask, request, jsonify, send_file
import pickle
import numpy as np

# Load the trained Random Forest model and LabelEncoder
rf_model = pickle.load(open('RandomForest.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from request
        data = request.json
        input_features = np.array([[float(data['nitrogen']), float(data['phosphorous']), float(data['potassium']),
                                    float(data['temperature']), float(data['humidity']),
                                    float(data['ph']), float(data['rainfall'])]])

        # Predict using the model
        prediction = rf_model.predict(input_features)
        crop_name = label_encoder.inverse_transform(prediction)[0]  # Decode the label

        return jsonify({'crop': crop_name}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
