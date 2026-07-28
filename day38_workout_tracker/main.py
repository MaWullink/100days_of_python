import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NUTRITION_API_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")
TOKEN = os.getenv("TOKEN")

base_url = "https://app.100daysofpython.dev"
nutrition_api_endpoint = "/v1/nutrition/natural/exercise"

sheety_endpoint = "https://api.sheety.co/37fdd29168e51f930e0371f9183c20ac/myWorkouts/workouts"

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print("Welcome to the Workout Tracker")

user_height = int(input("What is your height in cm? "))
user_weight = int(input("What is your weight in kg? "))
user_age = int(input("What is your age? "))
user_gender = input("Are you 'male' or 'female'? ")

while True:
    user_exercise = input("Describe your exercise (or type 'exit' to stop): ")

    if user_exercise.lower() == "exit":
        break

    body = {
        "query": user_exercise,
        "weight_kg": user_weight,
        "height_cm": user_height,
        "age": user_age,
        "gender": user_gender,
    }

    res = requests.post(
        url=base_url + nutrition_api_endpoint,
        json=body,
        headers=nutrition_headers
    )
    res.raise_for_status()

    data = res.json()

    exercise = data["exercises"][0]

    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    name = exercise["name"]

    today = dt.datetime.now()

    sheety_body = {
        "workout": {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(
        url=sheety_endpoint,
        json=sheety_body,
        headers=sheety_headers
    )
    response.raise_for_status()

    print(f"Added: {name} | {duration} min | {calories} calories")


