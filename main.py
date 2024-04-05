import requests

url_weather = "https://wttr.in/"

# города для вывода погоды
sheremetyevo = "svo"
london = "london"
сherepovets = "Череповец"

view_options = "?lang=ru&?M&?n&?q&?T"

sheremetyevo_weather = requests.get(url_weather + sheremetyevo + view_options)
london_weather = requests.get(url_weather + london + view_options)
сherepovets_weather = requests.get(url_weather + сherepovets + view_options)


def display_weather_info(place_url):
    print((place_url).text)


if __name__ == '__main__':
    display_weather_info(sheremetyevo_weather)
    display_weather_info(london_weather)
    display_weather_info(сherepovets_weather)
