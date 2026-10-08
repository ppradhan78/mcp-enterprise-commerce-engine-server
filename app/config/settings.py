import os

from dotenv import load_dotenv

load_dotenv()


class WeatherConfig:

    API_KEY = os.getenv("WEATHER_API_KEY")

    API_URL = os.getenv(
        "WEATHER_API_URL",
        "https://api.openweathermap.org/data/2.5/weather"
    )

class NorthWindConfig:
    BASE_API_URL = os.getenv("NORTHWIND_BASE_API_URL")

    if not BASE_API_URL:
        raise ValueError(
            "NORTHWIND_BASE_API_URL is not configured"
        )