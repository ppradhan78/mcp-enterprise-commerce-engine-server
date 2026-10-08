import logging

import httpx

from app.config.settings import WeatherConfig


logger = logging.getLogger(__name__)


class WeatherClient:

    def __init__(self):
        self.api_url = WeatherConfig.API_URL
        self.api_key = WeatherConfig.API_KEY

    async def get_weather(
        self,
        city: str,
        country_code: str
    ) -> dict:

        params = {
            "q": f"{city},{country_code}",
            "appid": self.api_key
        }

        logger.info(
            "Fetching weather data for %s, %s",
            city,
            country_code
        )

        async with httpx.AsyncClient(timeout=10.0) as client:

            response = await client.get(
                self.api_url,
                params=params
            )

            logger.info(
                "Weather API response status: %s",
                response.status_code
            )

            response.raise_for_status()

            return response.json()