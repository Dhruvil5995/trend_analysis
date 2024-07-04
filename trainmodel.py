import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import seaborn as sns
from prophet import Prophet
import joblib

pd.set_option('display.max_columns', None)
data = pd.read_csv('customer_shopping_data.csv')
#print(data)

data['invoice_date'] = pd.to_datetime(data['invoice_date'], dayfirst=True, errors='coerce')
#print(data)

data['total_sales'] = data['quantity'] * data['price']

#print(data)


aggregated_data = data.groupby(['invoice_date', 'category'])['total_sales'].sum().reset_index()
#print('check',aggregated_data[5:20])


aggregated_data['day_of_week'] = aggregated_data['invoice_date'].dt.dayofweek
aggregated_data['month'] = aggregated_data['invoice_date'].dt.month
aggregated_data['year'] = aggregated_data['invoice_date'].dt.year

#print('check2',aggregated_data[5:20])


category_data = aggregated_data[aggregated_data['category'] == 'Clothing']
#print(category_data)

category_data = category_data[['invoice_date', 'total_sales']]
category_data.rename(columns={'invoice_date': 'ds', 'total_sales': 'y'}, inplace=True)
print(category_data)

model = Prophet()
model.fit(category_data)

joblib_file = "prophet.pkl"
joblib.dump(model, joblib_file)