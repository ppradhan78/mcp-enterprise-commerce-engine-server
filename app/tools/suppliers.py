from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient


client = NorthwindClient()


async def get_suppliers(
    supplier_id: Optional[int] = None,
) -> Any:
    """
    Get suppliers.

    If supplier_id is provided, return one supplier.
    Otherwise return all suppliers.
    """

    if supplier_id is not None:

        return await client.get(
            f"/Suppliers/{supplier_id}"
        )

    return await client.get(
        "/Suppliers"
    )


async def search_suppliers(
    search: str,
) -> Any:
    """
    Search suppliers.
    """

    suppliers = await client.get(
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