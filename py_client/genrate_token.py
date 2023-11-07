import requests
from getpass import getpass
import json
auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})

if auth_response.status_code == 200:
    response_data = auth_response.json()
    filename = "token.json"

    with open(filename, 'w') as json_file:
        json.dump(response_data, json_file)

    print(f"Authentication successful. JSON response saved to {filename}")
else:
    print(f"Authentication failed with status code: {auth_response.status_code}")

