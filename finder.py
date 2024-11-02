import requests


class Finder:
    def __init__(self, keys, url):
        self.api_keys_list = keys
        self.key_index = 0
        self.domain = "N/A"
        self.params = {}
        self.data = None
        self.contacts = []
        self.url = url

        pass

    def request_server(self, domain):
        # For debugging
        print("API Key number: " + str(self.key_index + 1) + " is in use!")
        # Assign params attribute
        self.params = {
            "domain": domain,
            "api_key": self.api_keys_list[self.key_index]
        }
        # Request server
        response = requests.get(self.url, params=self.params)

        # Get response from the server
        self.data = response.json()

        # Extracting emails from the response
        if response.status_code == 200:
            self.contacts = [contact for contact in self.data["data"]["emails"]]
            print("GREAT! Email found from Hunter.io!!")
        else:
            # If the api key run out of credit then use the next api key
            if (self.data["errors"] and self.data["errors"][0]["id"] == "too_many_requests"):
                print("You are running out of credits, please subscribe to get more credits!")

                # Increment key index to choose the next api key from the api keys list
                self.key_index += 1

                # Request server recursively
                self.request_server(domain)
            else:
                print("Error:", response.json())

    def find_contacts(self):
        return self.contacts


    def check_hunterio_credits(self):
        url = f"https://api.hunter.io/v2/account?api_key={self.api_keys_list[self.key_index]}"  # replace with the actual URL you want to request
        try:
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Success!")
                print("Response content:", response.text)  # or response.json() if it returns JSON
            else:
                print(f"Request failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)