from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load the trained pipeline
pipeline = joblib.load('model_pipeline.pkl')

@app.get("/")
def read_root():
   return {"message": "Welcome to the FastAPI MLOps API!"}

@app.get("/favicon.ico")
def favicon():
   return {"message": "Favicon not available."}

@app.post("/predict/")
def predict(features: dict):
   # Convert input dictionary to DataFrame
   input_data = pd.DataFrame([features])
   # Make prediction
   prediction = pipeline.predict(input_data)
   return {"prediction": int(prediction[0])}
