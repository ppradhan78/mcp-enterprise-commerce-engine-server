from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient


client = NorthwindClient()


async def get_categories(
    category_id: Optional[int] = None,
) -> Any:
    """
    Get categories.

    If category_id is provided, return one category.
    Otherwise return all categories.
    """

    if category_id is not None:

        return await client.get(
            f"/Categories/{category_id}"
        )

    return await client.get(
        "/Categories"
    )


async def search_categories(
    search: str,
) -> Any:
    """
    Search categories by name or description.
    """

    categories = await client.get(
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