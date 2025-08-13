import requests


class DataManager:
    def __init__(self, sheety_endpoint, sheety_token):
        self.destination_data = {}
        self.sheety_endpoint = sheety_endpoint
        self.sheety_token = sheety_token

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {self.sheety_token}"
        }
        response = requests.get(self.sheety_endpoint, headers=headers)
        response.raise_for_status()
        print(response.status_code)
        self.destination_data = response.json()["prices"]
        return self.destination_data