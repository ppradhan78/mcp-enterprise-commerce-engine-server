from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient
from app.mcp_server import mcp


client = NorthwindClient()

@mcp.tool()
async def get_products(
    product_id: Optional[int] = None,
) -> Any:
    """
    Get products.

    If product_id is supplied, return one product.
    Otherwise return all products.
    """

    if product_id is not None:

        return  client.get(
            f"/Products/{product_id}"
        )

    return  client.get(
        "/Products"
    )


@mcp.tool()
async def search_products(
    search: str,
) -> Any:
    """
    Search products.
    """

    products =  client.get(
        "/Products"
    )

    if not isinstance(products, list):
        return products

    search_lower = search.lower()

    return [
        product
        for product in products
        if search_lower in str(product).lower()
    ]

@mcp.tool()
async def get_products_by_category(
    category_id: int,
) -> Any:
    """
    Get products belonging to a category.
    """

    products =  client.get(
        "/Products"
    )

    if not isinstance(products, list):
        return products

    results = []

    for product in products:

        if (
            product.get("categoryId")
            == category_id
        ):
            results.append(product)

    return results