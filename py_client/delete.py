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

product_id = input("What is the product id you want to delete ? = \n")
try:
    product_id = int(product_id)
except:
    product_id=None
    print(f'{product_id} not a valid id')
if product_id:

    endponts=f"http://localhost:8000/api/product/{product_id}/delete"
    get_response = requests.delete(endponts,headers=headers)
    print(get_response.status_code,get_response.status_code==204)