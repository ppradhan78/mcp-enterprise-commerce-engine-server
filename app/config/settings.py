import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    northwind_base_url: str
    northwind_timeout: float
    mcp_server_name: str
    log_level: str
    weather_api_url: str
    weather_api_key: str | None


def get_settings() -> Settings:

    northwind_base_url = os.getenv(
        "NORTHWIND_BASE_API_URL",
        "https://data-northwind.indigo.design",
    ).rstrip("/")

    northwind_timeout = float(
        os.getenv(
            "NORTHWIND_TIMEOUT",
            "30",
        )
    )

    mcp_server_name = os.getenv(
        "MCP_SERVER_NAME",
        "mcp-enterprise-commerce-engine-server",
    )

    log_level = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )

    weather_api_url = os.getenv(
        "WEATHER_API_URL",
        "https://api.openweathermap.org/data/2.5/weather",
    )

    weather_api_key = os.getenv(
        "WEATHER_API_KEY"
    )

    return Settings(
        northwind_base_url=northwind_base_url,
        northwind_timeout=northwind_timeout,
        mcp_server_name=mcp_server_name,
        log_level=log_level,
        weather_api_url=weather_api_url,
        weather_api_key=weather_api_key,
    )


settings = get_settings()