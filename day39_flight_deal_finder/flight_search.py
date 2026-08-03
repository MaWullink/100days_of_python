import os
import requests
from dotenv import load_dotenv


load_dotenv()


class FlightSearch:

    def __init__(self):
        self.endpoint = "https://serpapi.com/search"
        self.api_key = os.environ["SERP_APIKEY"]

    def check_flights(
        self,
        origin_city_code,
        destination_city_code,
        from_time,
        to_time
    ):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "EUR",
            "api_key": self.api_key,
        }

        response = requests.get(
            url=self.endpoint,
            params=params
        )

        response.raise_for_status()

        data = response.json()

        if "error" in data:
            print(data["error"])
            return None

        return data


