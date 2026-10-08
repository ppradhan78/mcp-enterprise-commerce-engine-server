import requests

from app.config import settings


class NorthwindClient:

    def __init__(self):
        self.base_url = settings.northwind_base_url
        self.timeout = settings.northwind_timeout

    def get(self, endpoint: str):

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = requests.get(
            url,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()