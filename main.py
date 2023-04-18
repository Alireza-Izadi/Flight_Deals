from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#Enter your desired origin city iata code and get the best deals available to your email address
origin_city = input("Please enter the IATA code of your Origin City: ")
ORIGIN_CITY_IATA = origin_city

#Adding destinations IATA code
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

#Calculating tomorrow time and sixmonth_time
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

#Find all the flights to the destination from tomorrow until 6 month later
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

#Check if the price is lower than the price in google sheet
if flight.price < destination["lowestPrice"]:
    notification_manager.send_email(price=flight.price, origin_city=flight.origin_city, origin_airport=flight.origin_airport, destination_city=flight.destination_city, destination_airport=flight.destination_airport, out_date=flight.out_date, return_date=flight.return_date)