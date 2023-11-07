import requests
import json
json_file_path = r"D:\ShankarDas\DRF\py_client\token.json"
try:
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        token = data['token']
except FileNotFoundError:
    print(f"The file '{json_file_path}' does not exist.")
except json.JSONDecodeError:
    print(f"The file '{json_file_path}' is not valid JSON.")


headers = {"Authorization": f"Bearer {token}"}
endpoint = "http://localhost:8000/api/product/" 

get_response = requests.get(endpoint, headers=headers)
    
data = get_response.json()
next_url = data['next']
results = data['results']
print("Next_URL", next_url)
print(results)