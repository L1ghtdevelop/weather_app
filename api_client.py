import os
import requests

from dotenv import load_dotenv

load_dotenv()



class ControllerAPI:
    def __init__(self) -> None:
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city: str) -> dict | None:
        try:
            params:dict = {
                "q": city,
                "appid": self.api_key,
                "units": "metric",
                "lang": "ru"
            }
            response: requests.Response = requests.get(self.base_url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"❌ Город '{city}' не найден!")
                return None

            else:
                print(f"Error fetching weather data: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching weather data: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def format_weather_data(self, data: dict) -> str:
        """Форматирование данных для вывода"""
        if not data:
            return ""

        city = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return f"""
    ╔══════════════════════════════════════╗
        🌍 Погода в городе: {city}
    ╠══════════════════════════════════════╣
        🌡️  Температура: {temp}°C
        🤚 Ощущается как: {feels_like}°C
        ☁️  Описание: {description.capitalize()}
        💧 Влажность: {humidity}%
        💨 Ветер: {wind_speed} м/с
    ╚══════════════════════════════════════╝
    """