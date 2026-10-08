from typing import Any

from app.mcp_server import mcp
from app.clients.northwind_client import NorthwindClient


client = NorthwindClient()


@mcp.tool()
async def get_customers(
    customer_id: str = "",
) -> Any:
    """
    Get Northwind customers.

    If customer_id is supplied, return a specific customer.
    Otherwise return all customers.
    """

    if customer_id:
        return  await client.get(
            f"/Customers/{customer_id}"
        )

    return  await client.get(
        "/Customers"
    )


@mcp.tool()
async def search_customers(
    search: str,
) -> Any:
    """
    Search customers by customer name or related customer fields.
    """

    customers =  await client.get(
        "/Customers"
    )

    if not isinstance(customers, list):
        return customers

    search_lower = search.lower()

    results = []

    for customer in customers:

        text = str(customer).lower()

        if search_lower in text:
            results.append(customer)

    return results