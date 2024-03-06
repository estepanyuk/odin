import config
import requests
import json

API_key = config.API_key

res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Kemerovo&appid={API_key}&units=metric').json()

print(json.dumps(res, indent=4))