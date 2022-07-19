import requests
import os
from twilio.rest import Client

api_key = os.environ.get('OWN_API_KEY')
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

parameters = {
    'lat' : 0,
    'lon': 0,
    'appid' : api_key,
    'exclude': 'current,minutely,daily'
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)

weather = request.json()['hourly'][:12]

will_rain = False

for i in weather:
    id = i['weather'][0]['id']
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an Umbrella", 
            from_="",
            to=""
            )
    print(message.status)
