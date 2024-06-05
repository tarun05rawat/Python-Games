import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NATURAL_LANGUAGE_EXERCISE_ENDPOINT = os.getenv("NATURAL_LANGUAGE_EXERCISE_ENDPOINT")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 173
AGE = 18

exercise_text = input("Tell me about today's workout: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

natural_language_exercise_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(url=NATURAL_LANGUAGE_EXERCISE_ENDPOINT, json=natural_language_exercise_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    print(exercise["name"].title())
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=headers)
    print(sheet_response.text)
