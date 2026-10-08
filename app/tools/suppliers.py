from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient
from app.mcp_server import mcp


client = NorthwindClient()

@mcp.tool()

async def get_suppliers(
    supplier_id: Optional[int] = None,
) -> Any:
    """
    Get suppliers.

    If supplier_id is provided, return one supplier.
    Otherwise return all suppliers.
    """

    if supplier_id is not None:

        return  client.get(
            f"/Suppliers/{supplier_id}"
        )

    return  client.get(
        "/Suppliers"
    )

@mcp.tool()
async def search_suppliers(
    search: str,
) -> Any:
    """
    Search suppliers.
    """

    suppliers =  client.get(
        "/Suppliers"
    )

    if not isinstance(suppliers, list):
        return suppliers

    search_lower = search.lower()

    return [
        supplier
        for supplier in suppliers
        if search_lower in str(supplier).lower()
    ]