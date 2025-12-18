import config
import requests

API_KEY = config.NUTRITION_AND_EXERCISE_API["api_key"]
APP_ID = config.NUTRITION_AND_EXERCISE_API["app_id"]

# TODO: print the exercise stats for plain text input.
request_url = f"{config.NUTRITION_AND_EXERCISE_API["base_url"]}{config.NUTRITION_AND_EXERCISE_API["calories_burned_endpoint"]}"

headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID
}

request_body = {
    "query": str(input("Tell me which exercise you did:\n")),
    "weight_kg": config.ATHLETE["weight_kg"],
    "height_cm": config.ATHLETE["height_cm"],
    "age": config.ATHLETE["age"],
    "gender": config.ATHLETE["gender"]
}

response = requests.post(request_url, json=request_body, headers=headers)
response.raise_for_status()

print(response.text)