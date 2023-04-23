import requests

# GET Method
api_url = "https://reqres.in/api/users?page=1"
#api_url = "https://reqres.in/api/users/2"
#api_url = "https://reqres.in/api/users/25"
response = requests.get(api_url)   #  ,auth = HTTPBasicAuth('user', 'pass')
print(response.status_code)
print(response.json())

print("****************************************")

# POST Method
api_url = "https://reqres.in/api/users"
newvalue = {"first_name": "Arockia", "last_name": "Neo"}
response = requests.post(api_url, json = newvalue)
print(response.status_code)
print(response.json())

# PUT Method
api_url = "https://reqres.in/api/users/1"
toupdate = {"id": 1, "first_name": "Arockia", "last_name": "Neo"}
response = requests.put(api_url, json=toupdate)
print(response.status_code)
print(response.json())

# DELETE Method
api_url = "https://reqres.in/api/users/2"
response = requests.delete(api_url)
print(response.status_code)
