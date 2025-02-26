import requests
import json
from constants import register_endpoint


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

        response = requests.post(register_endpoint, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            result = response.json()
            return True
        else:
            return f"Error: {response.json()['message']}"