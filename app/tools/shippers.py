
from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient
from app.mcp_server import mcp


client = NorthwindClient()

@mcp.tool()
async def get_shippers(
    shipper_id: Optional[int] = None,
) -> Any:
    """
    Get shippers.

    If shipper_id is provided, return one shipper.
    Otherwise return all shippers.
    """

    if shipper_id is not None:
        return  client.get(
            f"/Shippers/{shipper_id}"
        )

    return  client.get(
        "/Shippers"
    )

@mcp.tool()
async def search_shippers(
    search: str,
) -> Any:
    """
    Search shippers by name or any matching field.
    """

    shippers =  client.get(
        "/Shippers"
    )

    if not isinstance(shippers, list):
        return shippers

    search_lower = search.lower()

    return [
        shipper
        for shipper in shippers
        if search_lower in str(shipper).lower()
    ]