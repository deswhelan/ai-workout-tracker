import config
import requests

def get_nutrition_and_exercise_data():
    """Returns a dictionary representing exercise data determined by posting user input to an external nutrition and exercise AI"""
    request_url = f"{config.NUTRITION_AND_EXERCISE_API["base_url"]}{config.NUTRITION_AND_EXERCISE_API["calories_burned_endpoint"]}"

    headers = {
        "x-app-key": config.NUTRITION_AND_EXERCISE_API["api_key"],
        "x-app-id": config.NUTRITION_AND_EXERCISE_API["app_id"]
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

    return response.json()

def get_sheet_rows():
    request_url = config.SHEETY["endpoint"]

    headers = {
        "Authorization": f"Bearer {config.SHEETY["bearer_token"]}",
    }

    # request_body = {
    #     "query": str(input("Tell me which exercise you did:\n")),
    #     "weight_kg": config.ATHLETE["weight_kg"],
    #     "height_cm": config.ATHLETE["height_cm"],
    #     "age": config.ATHLETE["age"],
    #     "gender": config.ATHLETE["gender"]
    # }

    response = requests.get(request_url, headers=headers)
    response.raise_for_status()

    return response.json()

# get_nutrition_and_exercise_data()
print(get_sheet_rows())