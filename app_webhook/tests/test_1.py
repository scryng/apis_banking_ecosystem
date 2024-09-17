import sys
import os
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import settings, logger

json_data = {
    "time": "2024-08-27T14:55:00",
    "body": {
        "person_id": 1,
        "name": "Username",
        "email": "useremail@gmail.com",
        "gender": "M",
        "birth_date": "2000/01/01",
        "address": "Balneário-SC",
        "salary": "9.990",
        "cpf": "542.952.678-99"
    },
    "event": "person"
}

try:
    """
    Sends a POST request to the /person endpoint with a sample JSON payload.
    
    Constructs the URL using the API host and port from the settings and sends a POST request.
    If the request is successful, logs the status code and response JSON. If an error occurs,
    logs the error message.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    """
    url = f"http://{settings.api_host}:{settings.api_port}/person"
    response = requests.post(url, json=json_data)
    response.raise_for_status()
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")
except requests.exceptions.RequestException as e:
    logger.info(f"An error occurred: {e}")