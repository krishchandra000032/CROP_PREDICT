from django.shortcuts import render
from django.http import JsonResponse
from .models import CropPrediction
from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()
model.fit([[30, 100, 1], [32, 120, 2]], [0, 1]) # Dummy data

def index(request):
    return render(request, 'index.html')

def predict_crop(request):
    if request.method == "POST":
        temperature = float(request.POST['temperature'])
        rainfall = float(request.POST['rainfall'])
        soil_type = int(request.POST['soil_type'])

        prediction = model.predict(np.array([[temperature, rainfall, soil_type]]))
        return JsonResponse({'predicted_crop': prediction[0]})

