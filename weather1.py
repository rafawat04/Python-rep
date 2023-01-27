import json
import requests


URL = 'https://weather.tsukumijima.net/api/forecast/city/130010'
res = requests.get(URL)
data = json.loads(res.text)
# print(data['description'], data['text'])
print(data)

print(data['description']['text'])

for d in data['forecasts']:
    print(f"{d['date']}{d['dateLabel']}{d['telop']}")
