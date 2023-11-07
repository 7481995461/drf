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

headers = {'Authorization': f'Bearer {token}'}

data={'title': "Lenovo",
      'content': 'This is best Lenovo Laptop in the market',
      'body' : 'This is best Lenovo Laptop in the market',
      'price': '12000.00'
      }


endponts="http://localhost:8000/api/product/5/update"
get_response = requests.put(endponts,json=data,headers=headers)
print(get_response.json())