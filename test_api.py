import requests
import json

# Define the URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/predict"

# Define the request payload
payload = {
    "periods": 365
}

# Set the headers
headers = {
    "Content-Type": "application/json",
    "access_token": "b114ab40287f7431b0a0523f98ae47b1"
}

# Send the POST request
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Pretty-print the response
if response.status_code == 200:
    response_json = response.json()
    print("Status Code:", response.status_code)
    print("Response JSON:")
    print(json.dumps(response_json, indent=4, sort_keys=True))
else:
    print("Status Code:", response.status_code)
    print("Response JSON:", response.text)


#curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -H "access_token: b114ab40287f7431b0a0523f98ae47b1" -d "{\"periods\": 365}"
