import requests
import json
import io

URL = "http://127.0.0.1:8000/student_api1/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    r = requests.get(url=URL, params=data)
    if r.status_code == 200:
        try:
            data = r.json()  # Attempt to decode JSON response
            print(data)
        except requests.exceptions.JSONDecodeError:
            print("Response body is not valid JSON")
    else:
        print(f"Request failed with status code {r.status_code}")

# get_data(1)
        
def post_data():
    data = {
        'roll': 3,
        'name': 'raj',
        'city': 'pune'
    }
    
    headers = {'Content-Type': 'application/json'}  # Set Content-Type header to indicate JSON data
    json_data = json.dumps(data)  # Convert data to JSON string
    r = requests.post(url=URL, data=json_data, headers=headers)
    
    if r.status_code == 200:  
        print("Data successfully saved")
    else:
        print(f"Failed to save data, status code: {r.status_code}")

# post_data()
        
def update_data():
    data = {
        'id':11,
        'roll':4,
        'name': 'manoj',
        'city': 'dhakli'
    }
    try:
        json_data = json.dumps(data)  # Convert data to JSON string
        r = requests.put(url=URL, data=json_data)  # Send JSON data in the request body
        if r.status_code == 201:  # Assuming the server responds with status code 201 upon successful creation
            print("Data successfully saved")
        else:
            print(f"Failed to save data, status code: {r.status_code}")
            print(f"Response content: {r.text}")  # Print response content for debugging
    except requests.RequestException as e:
        print(f"Failed to send POST request: {e}")

# update_data()
        
def deleted_data():
    data = {
        'id':11
    }
    try:
        json_data = json.dumps(data)  # Convert data to JSON string
        r = requests.delete(url=URL, data=json_data)  # Send JSON data in the request body
        if r.status_code == 201:  # Assuming the server responds with status code 201 upon successful creation
            print("Data successfully saved")
        else:
            print(f"Failed to save data, status code: {r.status_code}")
            print(f"Response content: {r.text}")  # Print response content for debugging
    except requests.RequestException as e:
        print(f"Failed to send POST request: {e}")

deleted_data()