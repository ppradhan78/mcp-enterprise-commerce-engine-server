def test_server_import():

    from app.mcp_server import mcp

    assert mcp is not None


def test_client_import():

    from app.clients.northwind_client import (
        NorthwindClient,
    )

    client = NorthwindClient()

    assert client is not None


def test_settings():

    from app.config import settings

    assert settings.northwind_base_url