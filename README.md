# Sales Forecasting API (Trend Analysis)

This project provides a sales forecasting API using FastAPI, Prophet for time series forecasting, and other relevant Python libraries. The API is secured with an API key for authentication.

## Project Structure

- `trainmodel.py`: Script to train the model and save it using joblib.
- `main1.py`: Script to load the model and visualize the predictions.
- `fast.py`: FastAPI application with an endpoint to predict future sales.
- `test_api.py`: Script to test the API using the `requests` library.
- `requirements.txt`: Lists all the dependencies required for the project.
- `apikey.py`: Script to generate an API key.

## Setup Instructions

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```sh
   git clone [https://github.com/yourusername/sales-forecasting-api.git](https://github.com/Dhruvil5995/trend_analysis)
   cd sales-forecasting-api

2. **Install the dependencies:**

   ```sh
     pip install -r requirements.txt



3. **Generate an API key:**

   ```sh
   python apikey.py



4. **Train the model:**

   ```sh
    python trainmodel.py


### Running the Application

1. **Start the FastAPI application:**

   ```sh
  uvicorn fast:app --reload

  The application will be available at http://127.0.0.1:8000.

 2. **Test the API:**

   ```sh
  python test_api.py


##### You can also use curl:

```sh
  curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -H "access_token: b114ab40287f7431b0a0523f98ae47b1" -d "{\"periods\": 365}"

## Project Files
trainmodel.py
This script reads the customer shopping data, processes it, and trains a Prophet model to predict future sales. The trained model is saved using joblib.

main1.py
This script loads the pre-trained model and uses it to make future predictions, which are then visualized using matplotlib.

fast.py
This FastAPI application provides an endpoint to predict future sales. The endpoint is secured with an API key.























   
