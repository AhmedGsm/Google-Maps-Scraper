import json
import requests
from constants import *

class SnovioFinder:
    def __init__(self, api_keys):
        self.api_keys = api_keys
        self.key_index = 0

    def get_access_token(self):
        api_key = SNOV_API_KEYS_LIST[self.key_index]
        params = {
            'grant_type': 'client_credentials',
            'client_id': self.api_keys[self.key_index]["client_id"],
            'client_secret': self.api_keys[self.key_index]["client_secret"]
        }

        res = requests.post('https://api.snov.io/v1/oauth/access_token', data=params)
        resText = res.text.encode('ascii', 'ignore')

        return json.loads(resText)['access_token']

    def get_domain_search(self, website):
        # Base case to end recursive function
        if self.key_index == len(self.api_keys):
            return []
        token = self.get_access_token()
        params = {
            'access_token': token,
            'domain': website,
            'type': 'all',
            'limit': 10,
            'lastId': 0,
            # 'positions[]': ['Software Developer','QA']
        }

        res = requests.get('https://api.snov.io/v2/domain-emails-with-info', params=params)
        # If the api key is requests limited then jump to the next
        try:
            if json.loads(res.text)["errors"][0]["user_id"]:
                self.key_index += 1
                return self.get_domain_search(website)
        except:
            print("SNOVIO APi key number: " + str(self.key_index + 1) + " is used!")
            return json.loads(res.text)