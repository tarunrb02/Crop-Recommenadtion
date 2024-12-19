import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the dataset
crop_data = "crop_recommendation.csv"
df = pd.read_csv(crop_data)

# Features and target selection
features = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']

# Encode the target labels
label_encoder = LabelEncoder()
target_encoded = label_encoder.fit_transform(target)

# Save LabelEncoder
with open('label_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoder, file)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(features, target_encoded, test_size=0.2, random_state=42)

# Train Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)

# Save the Random Forest model
with open('RandomForest.pkl', 'wb') as file:
    pickle.dump(rf_model, file)

print("Model and Label Encoder saved successfully.")
