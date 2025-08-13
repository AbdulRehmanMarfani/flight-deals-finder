from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import os
from datetime import datetime, timedelta

sheety_endpoint = "https://api.sheety.co/bf38f748919877b14ed25682835c6ea7/flightDeals/prices"
amadeus_endpoint = "https://test.api.amadeus.com"
amadeus_api_key = os.environ.get("AMADEUS_API_KEY")
amadeus_api_secret = os.environ.get("AMADEUS_API_SECRET")



sheet_manager = DataManager(sheety_endpoint, os.environ.get("SHEETY_TOKEN"))
destination_data = sheet_manager.get_destination_data()
flightsearch = FlightSearch(amadeus_endpoint, amadeus_api_key, amadeus_api_secret)
flightdata = FlightData(amadeus_endpoint, amadeus_api_key, amadeus_api_secret)
access_token = flightdata.get_access_token()


IATA_code_origin = flightdata.get_IATA_code("Karachi", access_token)

for city in destination_data:
    IATA_code = flightdata.get_IATA_code(city["city"], access_token)
    if IATA_code:
        city["iataCode"] = IATA_code     

current = datetime.now()
tomorrow = (current + timedelta(days=1)).date()
six_months_date = (current + timedelta(30*6)).date()


for city in destination_data:
    flight = flightsearch.find_flights(
        origin=IATA_code_origin,
        destination=city["iataCode"],
        departure_date=tomorrow,
        return_date=six_months_date,
        access_token=access_token,
        max_price=city["lowestPrice"]
    )
    if flight["meta"]["count"] > 0:
        for offer in flight["data"]:
            print(f"Flight found from {IATA_code_origin} to {city['iataCode']} for {offer['price']['total']} {offer['price']['currency']} on {offer['itineraries'][0]['segments'][0]['departure']['at']}")
                # Here you can add code to send an email or notification
