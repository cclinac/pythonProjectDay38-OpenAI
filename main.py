import requests
import datetime as dt

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 172
AGE = 35
APP_ID = "60852238"
API_KEY = "148f09eb375ec9127b90bee4fd136821"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)


sheety_endpoint = "https://api.sheety.co/809b428ced075ed79fa674d0eb29cd8b/jimWorkouts/workouts"
s_headers = {
    "Authorization": "Basic Y2hpbGk4OTU6YTE5ODgxMTI4"
}
now = dt.datetime.now()
now_date = now.strftime("%x")
now_time = now.strftime("%X")
for _ in result['exercises']:
    sheet_input = {
                "workout": {
                    "date": now_date,
                    "time": now_time,
                    "exercise": _["name"].title(),
                    "duration": _["duration_min"],
                    "calories": _["nf_calories"]
                }
            }
    s_response = requests.post(sheety_endpoint, headers=s_headers, json=sheet_input)
    print(s_response)








