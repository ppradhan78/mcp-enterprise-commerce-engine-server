



from app.clients.weather_clients import WeatherClient


weather_client = WeatherClient()

def register_weather_tools(mcp):

    @mcp.tool()
    async def get_weather(
        city: str,
        country_code: str
    ):
        """
        Get weather information for a specific city and country.
        """

        return await weather_client.get_weather(
            city,
            country_code
        )