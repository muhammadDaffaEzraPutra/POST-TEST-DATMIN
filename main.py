from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI(title="Energy Production Prediction Model")

# Load model
try:
    with open("linear_regression_model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model features expected:", model.feature_names_in_)
except Exception as e:
    print("Error loading model:", str(e))
    raise RuntimeError("Failed to load model") from e

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODEL INPUT SESUAI FITUR ---
class InputData(BaseModel):
    Year: int = Field(..., example=2023)
    Hydroelectric_power: float = Field(..., example=5.0)
    Wind_wave_tidal: float = Field(..., example=8.0)
    Solar_photovoltaic: float = Field(..., example=3.5)
    Bioenergy: float = Field(..., example=6.0)

    class Config:
        fields = {
            'Hydroelectric_power': 'Hydroelectric power',
            'Wind_wave_tidal': 'Wind, wave, tidal',
            'Solar_photovoltaic': 'Solar photovoltaic',
        }

@app.get("/")
def read_root():
    return {"message": "Energy Production Prediction API is running"}

@app.get("/model-info")
def model_info():
    """Return information about the loaded model"""
    return {
        "model_type": str(type(model)),
        "expected_features": list(model.feature_names_in_),
        "n_features": model.n_features_in_,
        "model_params": model.get_params()
    }

@app.post("/predict")
async def predict(input_data: InputData):
    try:
        # Convert input ke DataFrame sesuai fitur yang diharapkan
        input_dict = {
            "Year": input_data.Year,
            "Hydroelectric power": input_data.Hydroelectric_power,
            "Wind, wave, tidal": input_data.Wind_wave_tidal,
            "Solar photovoltaic": input_data.Solar_photovoltaic,
            "Bioenergy": input_data.Bioenergy
        }
        input_df = pd.DataFrame([input_dict])

        # Predict
        prediction = model.predict(input_df)

        # Prediksi hasil
        return {
            "input": input_dict,
            "prediction_result": float(prediction[0]),
            "unit": "GWh",
            "model_version": "1.0"
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
