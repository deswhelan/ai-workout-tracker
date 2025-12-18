import config
import datetime as dt
import requests

def get_nutrition_and_exercise_data():
    """Returns a dictionary representing exercise data determined by posting user input to an external nutrition and exercise AI"""
    request_url = f"{config.NUTRITION_AND_EXERCISE_API["base_url"]}{config.NUTRITION_AND_EXERCISE_API["calories_burned_endpoint"]}"

    headers = {
        "x-app-key": config.NUTRITION_AND_EXERCISE_API["api_key"],
        "x-app-id": config.NUTRITION_AND_EXERCISE_API["app_id"]
    }

    request_body = {
        # "query": str(input("Tell me which exercise you did:\n")),
        "query": "I ran 5 miles",
        "weight_kg": config.ATHLETE["weight_kg"],
        "height_cm": config.ATHLETE["height_cm"],
        "age": config.ATHLETE["age"],
        "gender": config.ATHLETE["gender"]
    }

    response = requests.post(request_url, json=request_body, headers=headers)
    response.raise_for_status()
    print(f"Nutrition and Exercise API response status code: {response.status_code}")
    return response.json()

def save_workout_to_sheets():
    """Prompts user for text input representing a workout, converts to nutrition/exercise data via external API call, then saves data to Google Sheets via Sheety API"""
    request_url = config.SHEETY["endpoint"]

    headers = {
        "Authorization": f"Bearer {config.SHEETY["bearer_token"]}",
    }

    nutrition_and_exercise_data = get_nutrition_and_exercise_data()
    print(nutrition_and_exercise_data)

    request_body = {
        "workout": {
            "date": dt.datetime.now().strftime("%x"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": nutrition_and_exercise_data["exercises"][0]["name"],
            "duration": nutrition_and_exercise_data["exercises"][0]["duration_min"],
            "calories": nutrition_and_exercise_data["exercises"][0]["nf_calories"]
        }
    }

    response = requests.post(request_url, json=request_body, headers=headers)
    response.raise_for_status()
    print(f"Sheety response status code: {response.status_code}")

save_workout_to_sheets()