import requests_cache
from pprint import pprint
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


requests_cache.install_cache(
    "flight_cache",
    expire_after=3600
)

ORIGIN_AIRPORT = "AMS"


# Get destination data from Sheety
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


# Set search dates
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = tomorrow + timedelta(weeks=24)
return_date = six_months_from_today.strftime("%Y-%m-%d")


# Search flights
flight_search = FlightSearch()

for destination in sheet_data:

    print(f"Checking {destination['city']}")

    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_AIRPORT,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    cheapest_flight = find_cheapest_flight(
        flights,
        return_date
    )

    pprint(f"{destination['city']}: EUR {cheapest_flight.price}")

    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        print("Lower price found!")

        data_manager.update_lowest_price(
            destination["id"],
            cheapest_flight.price
        )
