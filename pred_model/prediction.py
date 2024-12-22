import numpy as np

def predict_crop(model, scaler, soil_encoder, state_encoder, crop_encoder, input_data):
    """Make a prediction for the crop type."""
    # Extract values from the DataFrame
    state = input_data['State'].values[0]
    rainfall = input_data['Rainfall'].values[0]
    ph = input_data['PH'].values[0]
    temperature = input_data['Temperature'].values[0]
    soil_type = input_data['Soil_type'].values[0]
    
    # Prepare the input data
    input_array = np.array([[state_encoder.transform([state])[0], rainfall, ph, temperature, soil_encoder.transform([soil_type])[0]]])
    
    # Scale the input data
    input_data_scaled = scaler.transform(input_array)
    
    # Make prediction
    predicted_crop_encoded = model.predict(input_data_scaled)
    
    # Return the predicted crop name
    return crop_encoder.inverse_transform(predicted_crop_encoded)[0]