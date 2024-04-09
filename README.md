#  Скрипт для вывода прогноза погоды в терминал

Данные о погоде берутся с сайта: https://wttr.in/

### Адрес документации сервиса wttr.in
https://wttr.in/:help

### Географические точки для вывода прогноза
Скрипт по-умолчанию выводит в терминал прогноз погоды для трех городов: Шереметьево, Лондон и Череповец.</br> 
Если вы хотите изменить географические точки для вывода прогноза, нужно в скрипте скорректировать список places_for_weather.</br> 
Смотрите поддерживаемые типы местоположений в документации сервиса https://wttr.in/:help</br> 

Ссылка на официальную документацию python по типу данных списки (list): https://docs.python.org/3/tutorial/introduction.html#lists

Все команды выполняются в терминале windows.

**Установка последней версии python:**
```
pip install python
```

**Для изоляции проекта рекомендуется развернуть виртуальное окружение:**
```
python -m venv env
```

**Активация виртуального окружения:**
```
.\env\Scripts\activate
```

**Клонируем репозиторий:**
```
git clone https://github.com/Chernykh-a-s/api-lesson-1-weather
```

**Переход в репозиторий со скриптом:**
cd api-lesson-1-weather

**Установка зависимостей:**
```
pip install -r requirements.txt
```

**Вывод погоды в терминал:**
```
python weather.py
```

![Пример скриншота](https://github.com/Chernykh-a-s/api-lesson-1-weather/blob/weather/Screenshot.png)

