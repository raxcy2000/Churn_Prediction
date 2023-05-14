import os

FILE_NAME = "Bank Customer Churn Prediction Data.csv"
DATA_FOLDER = "assets"

main_path = os.path.dirname(os.getcwd())
data_path = os.path.join(os.path.join(main_path, DATA_FOLDER), FILE_NAME)


autogluon_params = {
    "save_path": os.path.join(main_path, 'artefacts/model_autogluon'),
    "time_limit": 60,
    "label": "churn",
    "problem_type": "binary"
}