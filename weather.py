import requests
from requests.exceptions import HTTPError

weather_url = "https://wttr.in/"

places = ["svo", "london", "Череповец"]

params = {
    "lang": "ru",  # язык
    "M": "",  # скорость ветра в м/с
    "n": "",  # узкая версия (только день и ночь)
    "q": "",  # тихая версия (без текста "Прогноз погоды")
    "T": "",  # черно-белый прогноз (без цветов)
}


def fetch_weather_forecast(places, weather_url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


for place in places:
    url = f"{weather_url}{place}"
    fetch_weather_forecast(place, weather_url, params)

try:
    forecast = fetch_weather_forecast(places, weather_url, params)
except HTTPError as http_err:
    print(f"Ошибка ответа от {weather_url}: {http_err}")

if __name__ == '__main__':
    print(fetch_weather_forecast(places, weather_url, params))
