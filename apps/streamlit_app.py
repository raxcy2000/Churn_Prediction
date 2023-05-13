## This is going to be a Streamlit App

import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))

import streamlit as st
import pandas as pd
from parameters.parameters import autogluon_params
from autogluon.tabular import TabularPredictor

st.title('Churn Prediction')

credit_score = st.slider('credit_score', 350, 850)
country = st.selectbox("country", options=['France', 'Spain', 'Germany'])
gender = st.selectbox("sex", options=["male", "female"])
age = st.slider('age', 16, 100)
tenure = st.slider('tenure', 0, 10)
balance = st.slider('balance', 0.0, 300000.0)
products_number = st.selectbox("product_number", options=['1', '2', '3', '4'])
credit_card = st.selectbox("credit_card", options=['0', '1'])
active_member = st.selectbox("active_member", options=['0', '1'])
estimated_salary =  st.slider('estimated_salary', 0.0, 200000.0)

input_data_dict = {
    'credit_score': credit_score,
    'country': country,
    'gender': gender,
    'age': age,
    'tenure': tenure,
    'balance': balance,
    'products_number': products_number,
    'credit_card': credit_card,
    'active_member': active_member,
    'estimated_salary': estimated_salary
}

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = autogluon_params["save_path"]

save_model_predictor = TabularPredictor.load(save_path)

submit = st.button("CLICK TO PREDICT CHURN")

if submit:
    churn = save_model_predictor.predict(input_data)[0]
    st.write(f"The predicted churn possibility is: {churn}")