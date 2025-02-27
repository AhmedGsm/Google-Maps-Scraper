import requests
import json
from constants import *


class Register:

    def __init__(self, name, email, phone, mac_address):
        self.name = name
        self.email = email
        self.phone = phone
        self.mac_address = mac_address

    def request_Api(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "mac_address": self.mac_address,
        }

        # response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
        response = requests.post(f"{api_endpoint}?operation=register", headers=headers, json=json.dumps(data))

        if response.status_code == 201:
            result = response.json()
            return True
        else:
            return f"Error: {response.json()['message']}"

    # Function to register a user
    def register_user(self):
        data = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "mac_address": self.mac_address,
        }

        response = requests.post(f"{api_endpoint}?operation=register", json=json.dumps(data))
        if response.status_code == 201:
            result = response.json()
            return True
        else:
            return f"Error: {response.json()['message']}"

    # Function to read user data
    def read_user_data(self, user_id):
        response = requests.get(f"{api_endpoint}?operation=read&user_id={user_id}")
        print(response.json())

    # Function to modify user data
    def modify_user_data(self, user_id):
        data = {
            'user_id': user_id,
            'email': 'new.email@example.com',
            'mac_address': '00:14:22:01:23:46'
        }
        response = requests.put(f"{api_endpoint}?operation=modify", json=data)
        print(response.json())

