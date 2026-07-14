import requests
import smtplib
from datetime import datetime
import time

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "test"

MY_LAT = 52.161280 # Your latitude
MY_LONG = 6.394900 # Your longitude

# Get sunrise and sunset times
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


while True:
    # Get current ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    current_hour = datetime.now().hour

    # Your position is within +5 or -5 degrees of the ISS position
    if (abs(MY_LONG - iss_longitude) <= 5 and abs(MY_LAT - iss_latitude) <= 5) and (
            current_hour >= sunset or current_hour <= sunrise):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="test2@gmail.com",
                msg="Subject: ISS Alert 🚀\n\nLook Up👆\n\nThe ISS is passing by."
            )

    time.sleep(60)





