import requests

class FlightData:
    def __init__(self, amadeus_endpoint, amadeus_api_key, amadeus_api_secret):
        self.amadeus_endpoint = amadeus_endpoint
        self.amadeus_api_key = amadeus_api_key
        self.amadeus_api_secret = amadeus_api_secret

    def get_access_token(self):
        url = f"{self.amadeus_endpoint}/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_api_key,
            "client_secret": self.amadeus_api_secret
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_IATA_code(self, city_name, access_token):
        self.headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
        }
        parameters = {
            "keyword": city_name
        }
        response = requests.get(
            f"{self.amadeus_endpoint}/v1/reference-data/locations/cities",
            headers=self.headers,
            params=parameters
        )
        response.raise_for_status()
        print(response.status_code)
        data = response.json()
        if data["data"]:
            return data["data"][0]["iataCode"]
        else:
            print(f"No IATA code found for {city_name}.")
            return None
    pass