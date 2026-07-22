import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": 52.1614,
    "lon": 6.4156,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

res = requests.get(url, params=params)
data = res.json()

print(f"Status: {res.status_code}")
print("\n🌤️ Weather forecast:\n")

will_rain = False

for forecast in data["list"]:
    weather_id = forecast["weather"][0]["id"]
    description = forecast["weather"][0]["description"]
    temperature = forecast["main"]["temp"]

    time = forecast["dt_txt"].split(" ")[1]

    if weather_id < 700:
        emoji = "🌧️"
        will_rain = True
    elif weather_id < 800:
        emoji = "☁️"
    else:
        emoji = "☀️"

    print(f"{time} {emoji} {description.title()} - {temperature}°C")

print()

if will_rain:
    print("☔ Bring an umbrella today!")
else:
    print("😎 No rain expected. You're good to go!")