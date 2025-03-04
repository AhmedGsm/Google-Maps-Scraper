import requests
import json

from constants import api_endpoint


class LicenseManagerClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def _handle_response(self, response):
        try:
            data = response.json()
        except json.JSONDecodeError:
            return {"status": "error", "message": "Invalid JSON response"}

        if response.status_code == 200:
            return data
        return {
            "status": "error",
            "code": response.status_code,
            "message": data.get('message', 'Unknown error')
        }

    def register_device(self, user_data):
        payload = {
            "action": "register",
            "email": user_data['email'],
            "mac_address": user_data['mac_address'],
            "name": user_data.get('name', ''),
            "phone": user_data.get('phone', ''),
            "free_credits": user_data.get('free_credits', 0)
        }
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        return self._handle_response(response)

    def get_data(self, query):
        params = {'action': 'get_data', 'query': query}
        response = requests.get(
            self.base_url,
            headers=self.headers,
            params=params
        )
        return self._handle_response(response)

    def update_user(self, user_id, update_fields):
        payload = {
            "action": "update_user",
            "user_id": user_id,
            "update_fields": update_fields
        }
        response = requests.put(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        return self._handle_response(response)

    def delete_device(self, device_id):
        payload = {
            "action": "delete_device",
            "device_id": device_id
        }
        response = requests.delete(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        return self._handle_response(response)

    def check_license(self, user_id):
        """
        Check the license status for a user.
        """
        payload = {
            "action": "check_license",
            "user_id": user_id
        }
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        return self._handle_response(response)
"""
client = LicenseManagerClient(api_endpoint)
response = client.check_license(181)

print(response)
"""


