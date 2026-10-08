# from typing import Any, Optional

# from app.clients.northwind_client import NorthwindClient


# client = NorthwindClient()


# async def get_suppliers(
#     supplier_id: Optional[int] = None,
# ) -> Any:
#     """
#     Get suppliers.

#     If supplier_id is provided, return one supplier.
#     Otherwise return all suppliers.
#     """

#     if supplier_id is not None:

#         return await client.get(
#             f"/Suppliers/{supplier_id}"
#         )

#     return await client.get(
#         "/Suppliers"
#     )


# async def search_suppliers(
#     search: str,
# ) -> Any:
#     """
#     Search suppliers.
#     """

#     suppliers = await client.get(
#         "/Suppliers"
#     )

#     if not isinstance(suppliers, list):
#         return suppliers

#     search_lower = search.lower()

#     return [
#         supplier
#         for supplier in suppliers
#         if search_lower in str(supplier).lower()
#     ]

from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient


client = NorthwindClient()


async def get_shippers(
    shipper_id: Optional[int] = None,
) -> Any:
    """
    Get shippers.

    If shipper_id is provided, return one shipper.
    Otherwise return all shippers.
    """

    if shipper_id is not None:
        return await client.get(
            f"/Shippers/{shipper_id}"
        )

    return await client.get(
        "/Shippers"
    )


async def search_shippers(
    search: str,
) -> Any:
    """
    Search shippers by name or any matching field.
    """

    shippers = await client.get(
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