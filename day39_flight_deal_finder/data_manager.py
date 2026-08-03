import os
import requests
from dotenv import load_dotenv


load_dotenv()


class DataManager:

    def __init__(self):
        self.endpoint = os.environ["SHEETY_ENDPOINT"]
        self.headers = {
            "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }

    def get_destination_data(self):
        response = requests.get(
            url=self.endpoint,
            headers=self.headers
        )

        response.raise_for_status()

        data = response.json()

        return data["prices"]

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }

        response = requests.put(
            url=f"{self.endpoint}/{row_id}",
            json=new_data,
            headers=self.headers
        )

        response.raise_for_status()

