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


def get_settings() -> Settings:
    base_url = os.getenv(
        "NORTHWIND_BASE_URL",
        "https://data-northwind.indigo.design",
    ).rstrip("/")

    timeout = float(
        os.getenv("NORTHWIND_TIMEOUT", "30")
    )

    server_name = os.getenv(
        "MCP_SERVER_NAME",
        "mcp-enterprise-commerce-engine-server",
    )

    log_level = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )

    return Settings(
        northwind_base_url=base_url,
        northwind_timeout=timeout,
        mcp_server_name=server_name,
        log_level=log_level,
    )


settings = get_settings()