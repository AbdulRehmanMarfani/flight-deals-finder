import requests

class FlightSearch:
    def __init__(self, amadeus_endpoint, amadeus_api_key, amadeus_api_secret):
        self.amadeus_endpoint = amadeus_endpoint
        self.amadeus_api_key = amadeus_api_key
        self.amadeus_api_secret = amadeus_api_secret

    def find_flights(self, access_token, origin, destination, departure_date, return_date, max_price):
        url = f"{self.amadeus_endpoint}/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        parameters = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date, 
            "maxPrice": max_price,
            "adults": 1,
            "currencyCode": "GBP"
        }


        response = requests.get(url=url, headers=headers, params=parameters)
        response.raise_for_status()
        print(response.status_code)
        return response.json()
    


        
    