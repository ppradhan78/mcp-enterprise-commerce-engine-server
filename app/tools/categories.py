from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient
from app.mcp_server import mcp


client = NorthwindClient()

@mcp.tool()
async def get_categories(
    category_id: Optional[int] = None,
) -> Any:
    """
    Get categories.

    If category_id is provided, return one category.
    Otherwise return all categories.
    """

    if category_id is not None:

        return  client.get(
            f"/Categories/{category_id}"
        )

    return  client.get(
        "/Categories"
    )

@mcp.tool()
async def search_categories(
    search: str,
) -> Any:
    """
    Search categories by name or description.
    """

    categories =  client.get(
        "/Categories"
    )

    if not isinstance(categories, list):
        return categories

    search_lower = search.lower()

    return [
        category
        for category in categories
        if search_lower in str(category).lower()
    ]