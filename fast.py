from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
import pandas as pd
import joblib
from prophet import Prophet

API_KEY = "b114ab40287f7431b0a0523f98ae47b1"  # Replace with your API key
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI()

def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

# Load the pre-trained model
model = joblib.load("prophet.pkl")

# Define request body schema
class PredictRequest(BaseModel):
    periods: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sales Forecast API"}

@app.post("/predict")
def predict(request: PredictRequest, api_key: str = Depends(get_api_key)):
    try:
        # Make future predictions using the loaded model
        future = model.make_future_dataframe(periods=request.periods)
        forecast = model.predict(future)

        # Convert the forecast to a dictionary
        forecast_dict = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(request.periods).to_dict(orient='records')

        return {"forecast": forecast_dict}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
