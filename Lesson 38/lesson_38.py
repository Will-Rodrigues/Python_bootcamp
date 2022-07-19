import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('', '')

today_date = datetime.now().date()
today_time = datetime.now().time()

user_exercise = input("Tell me which exerciseyou did:\n")

NUTRITIONIX_ID = ''
NUTRITIONIX_KEY = ''

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
WORKOUT_SHEET = 'https://api.sheety.co/26bc21fcd40a254d6f5543abd3c3f910/myWorkouts/workouts'

headers = {
    'x-app-id': NUTRITIONIX_ID,
    'x-app-key': NUTRITIONIX_KEY
}

exercise_body = {
    "query": user_exercise,
    "gender": "male",
    "weight_kg": 83,
    "height_cm": 170,
    "age": 28
}

exercises = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=exercise_body, basic=basic)

for exercise in exercises.json()['exercises']:
    sheet_body = {
        'workout' : {
            'Date' : str(today_date),
            'Time' : str(today_time),
            'Exercise': exercise['name'].title(),
            'Duration': exercise['duration_min'],
            'Calories': exercise['nf_calories']
        }
    }

    sheet = requests.post(url=WORKOUT_SHEET, json=sheet_body)
    print(sheet.text)
