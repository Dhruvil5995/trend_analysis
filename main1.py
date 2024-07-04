import joblib
import matplotlib.pyplot as plt
from prophet import Prophet


loaded_model = joblib.load("E:\\task1\\prophet.pkl")


# Make future predictions using the loaded model
future = loaded_model.make_future_dataframe(periods=365)  # Forecasting for the next 365 days
forecast = loaded_model.predict(future)

# Plot the forecast
fig1 = loaded_model.plot(forecast)
plt.title('Total Sales Forecast for Clothing Category')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Plot the components
fig2 = loaded_model.plot_components(forecast)
plt.show()


