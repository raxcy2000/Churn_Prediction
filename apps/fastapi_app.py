import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))

import pandas as pd
from parameters.parameters import autogluon_params
from autogluon.tabular import TabularPredictor
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

#input_data_dict = request.form.values()
input_data_dict = [600, 'France', 'Male', 42, 2, 10000, 1, 1, 1, 10909]
input_data_dict = {'credit_score': 600, 'country': 'France', 'gender': 'Male', 'age': 42, 'tenure': 2, 'balance': 10000, 'products_number': 1, 'credit_card': 1, 'active_member': 1, 'estimated_salary':10909}

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

class PredictionRequest(BaseModel):
    credit_score: int
    country: str
    gender: str
    age: int
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float

    # Add more features as needed

class PredictionResponse(BaseModel):
    prediction: int
    #probability: float



@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    #input_data = pd.DataFrame(input_data_dict)
    data = pd.DataFrame([request.dict()])

    # input_data.columns = ['credit_score', 'country', 'gender', 'age', 'tenure', 
    # 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary']
    print("dd"*50, data)

    # input_data['balance'] = input_data['balance'].astype('float')
    # input_data['estimated_salary'] = input_data['estimated_salary'].astype('float')

    save_path = autogluon_params["save_path"]
    save_model_predictor = TabularPredictor.load(save_path)

    prediction = save_model_predictor.predict(data.iloc[[0]])
    print("vv"*50, prediction)

    response = PredictionResponse(prediction=prediction)
    return response
    #return churn





