import requests, os
from twilio.rest import Client

api_key = os.environ['API_KEY']
latitue = 18.593712
longitude = 73.831234
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

parameters = {
    'lat': latitue,
    'lon': longitude,
    'appid': api_key,
    'cnt': 4,
}
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

i = 0
will_rain = False
for i in range(4):
    condition_code = weather_data['list'][i]['weather'][0]['id']
    if condition_code <= 700:
        will_rain = True
        break
    i += 1
if will_rain:
    print('Bring an umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today, remember to bring an umbrella",
        to="whatsapp:+917021615621",
    )
    print(message.status)
