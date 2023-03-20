# 1. Написати програму, яка буде робити запит на один із 5 сайтів і друкувати статус-код відповіді, назву сайту, а
# також довжину HTML-коду із відповіді.
# Вибір сайту для здійснення запиту має бути здійснений випадковим чином (random).

import requests
import random

urls = ['google.com', 'facebook.com', 'twitter.com', 'amazon.com', 'apple.com']
url = f'https://{random.choice(urls)}'
res = requests.get(url)

print(f"Url is: {url}\n"
      f"Status-code is: {res.status_code}\n"
      f"Length of HTML response is: {len(res.content)}")

# 2. Використовуючи API для погоди https://open-meteo.com/en/docs, написати програму, яка буде приймати від користувача
# назву міста і виводити поточні показники погоди в консоль.


import requests

city = input('Enter name od the city: ')

url_geocoding = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
res_geocoding = requests.get(url_geocoding).json()
result_res_geocoding = res_geocoding.get('results')[0]

latitude = result_res_geocoding.get('latitude')
longitude = result_res_geocoding.get('longitude')

url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=True'
res = requests.get(url).json()
weather = res.get('current_weather')
print(f"Temperature is: {weather.get('temperature')} °C \n"
      f"Windspeed is: {weather.get('windspeed')} km/h,\n"
      f"Winddirection is: {weather.get('windspeed')} °")
