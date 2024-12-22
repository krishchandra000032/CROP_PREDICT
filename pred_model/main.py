import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from data_preprocessing import load_data, preprocess_data
from model_training import train_model
from prediction import predict_crop

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

# Load and preprocess data
file_path = 'D:/Academics/VIT/Project Exhibition - Final Review/pred_model/MOCK_DATA-3.csv'
data = load_data(file_path)
processed_data, soil_encoder, state_encoder, crop_encoder = preprocess_data(data)

# Define features and target variable
X = processed_data[['State', 'Rainfall', 'PH', 'Temperature', 'Soil_type']]  # Updated features
y = processed_data['Crop_name']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model
model, X_test, y_test = train_model(X_scaled, y)

# Evaluate the model
y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# report = classification_report(y_test, y_pred)

# print(f'Accuracy: {accuracy * 100:.2f}%')
# print('Classification Report:')
# print(report)
# Get input from command line arguments
state = sys.argv[1]
rainfall = float(sys.argv[2])
ph = float(sys.argv[3])
temperature = float(sys.argv[4])
soil_type = sys.argv[5]
# Example usage of prediction
# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'State': [state],
    'Rainfall': [rainfall],
    'PH': [ph],
    'Temperature': [temperature],
    'Soil_type': [soil_type]
})

predicted_crop = predict_crop(model, scaler, soil_encoder, state_encoder, crop_encoder, input_data)
print(predicted_crop, flush=True)