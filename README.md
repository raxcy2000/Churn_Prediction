# Churn_Prediction

### Introduction

Bank Customer Churn - Predict if a customer will leave or stay


### Dataset: 

Bank Customer Churn Dataset available [here](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset). It consist of 10,000 rows and 12 columns

This dataset is for ABC Multistate bank with following columns:

customer_id, credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary, and churn.

The `customer id` is unused, `churn` is the target variable while the other features are used as input. 

### Environment Setup

Create a `conda` environment

```python
conda create --name churnenv python=3.9 -y
```

Activate the environment

```python
conda activate churnenv
```

Install required packages in the environment using **requirements.txt** file.

```python
pip install -r requirements.txt
```
### Project Structure
```
Churn Prediction
|--README.md
|--artefacts
|--assets
|--data_ingestion
|--images
|--model_building
|--notebooks
|--requirements.txt
|--main.py
|--app.py
|--parameters
|--test
```

## Data Ingestion

## Exploratory Data Analysis (EDA)

## Features Engineering or Processing

## Model Building

## Model Evaluation

## Model Deployment

Deployment is done using [Streamlit](https://streamlit.io/) and Flask.

```python
streamlit run streamlit_app.py
```

```python
python flask_app.py
```

## References

- [Kaggle - Bank Customer Churn Dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)
- [Streamlit](https://streamlit.io/)
