import requests


class Finder:
    def __init__(self, key, url):
        self.api_key = key
        self.domain = "N/A"
        self.params = {}
        self.data = None
        self.contacts = []
        self.url = url

        pass

    def request_server(self,  domain):
        # Assign params attribute
        self.params = {
            "domain": domain,
            "api_key": self.api_key
        }
        # Request server
        response = requests.get(self.url, params=self.params)

        # Get response from the server
        self.data = response.json()

        # Extracting emails from the response
        if response.status_code == 200:
            self.contacts = [contact for contact in self.data["data"]["emails"]]
        else:
            print("Error:", response.json())

    def find_contacts(self):
        return self.contacts


    def check_hunterio_credits(self):
        url = f"https://api.hunter.io/v2/account?api_key={self.api_key}"  # replace with the actual URL you want to request
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
"""
# Test the class
API_KEY = "a32f0ffbdca8c63a0fb35db1e52a131cabc3b7c6"
# Hunter.io endpoint
url = f"https://api.hunter.io/v2/domain-search"
# Domain website
domain = "ventionteams.com"

# Instantiate finder class
finder = Finder(API_KEY, url)

# Request the server
finder.request_server(domain)

# Extract contacts details
contacts = finder.find_contacts()

# Loop through the contacts list
for c in contacts:
    print("Email: " + str(c["value"]) + "|")
    print("Type: " + str(c["type"]) + "|")
    print("Confidence: " + str(c["confidence"]) + "|")
    print("First name: " + str(c["first_name"]) + "|")
    print("Last name: " + str(c["last_name"]) + "|")
    print("Position: " + str(c["position"]) + "|")
    print("Seniority: " + str(c["seniority"]) + "|")
    print("Department: " + str(c["department"]) + "|")
    print("Linkedin: " + str(c["linkedin"]) + "|")
    print("Twitter: " + str(c["twitter"]) + "|")
    print("Phone number: " + str(c["phone_number"]) + "|")

# Check the remaining credits
finder.check_hunterio_credits()"""
