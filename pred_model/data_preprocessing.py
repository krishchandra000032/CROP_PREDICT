import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Preprocess the data by encoding categorical variables."""
    soil_encoder = LabelEncoder()  # Create an instance of LabelEncoder for soil type
    state_encoder = LabelEncoder()  # Create an instance of LabelEncoder for state names
    crop_encoder = LabelEncoder()    # Create an instance of LabelEncoder for crop names
    
    # Encode soil type
    data['Soil_type'] = soil_encoder.fit_transform(data['Soil_type'])
    
    # Encode crop names
    data['Crop_name'] = crop_encoder.fit_transform(data['Crop_name'])  # Encode crop names
    
    # Encode state names
    data['State'] = state_encoder.fit_transform(data['State'])  # Encode state names
    
    return data, soil_encoder, state_encoder, crop_encoder