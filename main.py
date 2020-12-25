import requests
import os
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
# go to openweathermap.org for your own api key
api_key = "<Your Own Weather map APi key>"
# got sign up for a free account on twilio for account sid and auth token
account_sid = "<add your twilio account_sid>"
auth_token = "<add your twilio auth_token>"

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api_key,
    "exclude": "daily,current,minutely"
}

response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for number in range(0, 12):
    condition_code = (weather_data["hourly"][number]["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="IT's going to rain today. Remember to bring an ☂",
        #you can get one free trial number form the twilio sign up
        from_="<add your free trial number here>",
        to="<add the phone number you want to send the code to!>"
    )
    print(message.status)
