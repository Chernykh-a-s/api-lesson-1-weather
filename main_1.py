import requests
from requests.exceptions import HTTPError

url_weather = "https://wttr.in/"

places_for_weather = ["svo", "london", "Череповец"]

request_params = {
    "lang": "ru",  # язык
    "M": "",  # скорость ветра в м/с
    "n": "",  # узкая версия (только день и ночь)
    "q": "",  # тихая версия (без текста "Прогноз погоды")
    "T": "",  # черно-белый прогноз (без цветов)
}


def weather_forecast(places_for_weather, url_weather, request_params):
    try:
        for place in places_for_weather:
            url = f"{url_weather}{place}"
            response = requests.get(url, params=request_params)
            response.raise_for_status()
            weather = response.text
            print(weather)
    except HTTPError as http_err:
        print(f"Ошибка ответа от {url_weather}: {http_err}")


if __name__ == '__main__':
    weather_forecast(places_for_weather, url_weather, request_params)
