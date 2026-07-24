import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = "graph1"


# Create user
pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# res = requests.post(url=pixela_endpoint, json=pixela_params)
# print(res.text)


# Create graph
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res.text)


# Add a pixel
today = dt.datetime.now()
current_date = today.strftime("%Y%m%d")

add_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

add_pixel_params = {
    "date": current_date,
    "quantity": "15",
}

# res = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
# print(res.text)


# Update a pixel
update_pixel_endpoint = (
    f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"
)

update_params = {
    "quantity": "10",
}

# res = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(res.text)


# Delete a pixel
delete_endpoint = (
    f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"
)

# res = requests.delete(url=delete_endpoint, headers=headers)
# print(res.text)
