from pprint import pprint
import requests
import os
SHEETY_PRICE_ENDPOINT = os.environ.get("SHEETY_PRICE_ENDPOINT")

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        '''Reading google sheet data through Sheety API'''
        response = requests.get(url=SHEETY_PRICE_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        '''Updating google sheet data using Sheety API'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)