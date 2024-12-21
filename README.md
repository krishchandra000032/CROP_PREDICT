# CROP_PREDICT
Project exhibition 1
# RUN THE DJANGO APPLICATION :
python3 manage.py runserver
Now, you can test the application locally at ( http://127.0.0.1:8000/predict/ )
# PREPARE FOR DEPLOYMENT:
Create a requirements.txt file to list all dependencies: 
1.Run this command in terminal/powershell
pip3 freeze > requirements.txt

# Deploy on Heroku:
Install Heroku CLI if you don’t have it.
Log in to Heroku:
heroku login
Create a Procfile to specify the command to run the app:
web: gunicorn crop_prediction.wsgi
Push to Heroku: Initialize Git, commit the code, and push to Heroku:
git init
heroku create
git add .
git commit -m "Initial commit"
git push heroku master
Step 5: Creating the README.md for GitHub

# README.md

# Crop Prediction Website

## Overview
This web application predicts which crop is suitable based on weather conditions (temperature, rainfall, and soil type) using a machine learning model (Linear Regression).

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/krishchandra000032/CROP_PREDICT.git
Install dependencies:
pip install -r requirements.txt
Run the Django development server:
python3 manage.py runserver
Navigate to http://127.0.0.1:8000/predict/ to use the application.
Deployment

This project is deployed on Heroku.

Technologies Used

Python
Django
Scikit-learn (for Linear Regression)
Heroku (for deployment)

#### Conclusion
After following these steps, you'll have a crop prediction website running locally and deployed on a cloud platform (e.g., Heroku). The model can be improved with better datasets and more advanced algorithms.
