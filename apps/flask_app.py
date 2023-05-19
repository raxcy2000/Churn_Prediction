import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))

import pandas as pd
from parameters.parameters import autogluon_params
from autogluon.tabular import TabularPredictor

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    input_data_dict = request.form.values()
    input_data = pd.DataFrame([input_data_dict])

    input_data.columns = ['credit_score', 'country', 'gender', 'age', 'tenure', 
    'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary']

    input_data['balance'] = input_data['balance'].astype('float')
    input_data['estimated_salary'] = input_data['estimated_salary'].astype('float')

    save_path = autogluon_params["save_path"]
    save_model_predictor = TabularPredictor.load(save_path)

    churn = save_model_predictor.predict(input_data.iloc[[0]])

    return render_template('index.html', prediction=churn[0])


if __name__ == '__main__':
    app.run(port=3000, debug=True)

