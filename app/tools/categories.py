from typing import Optional

from app.mcp_server import mcp
from app.clients.northwind_client import NorthwindClient
from app.models.category import Category, CategoryUpdate


client = NorthwindClient()


@mcp.tool()
async def get_categories(
    category_id: Optional[int] = None,
):
    """
    Get categories.

    If category_id is supplied, return one category.
    Otherwise return all categories.
    """

    if category_id is not None:
        return await client.get(
            f"/categories/{category_id}"
        )

    return await client.get(
        "/categories"
    )


@mcp.tool()
async def create_category(
    category: Category,
):
    """
    Create a new category.
    """

    return await client.post(
        "/categories",
        data=category.model_dump(exclude_none=True),
    )


@mcp.tool()
async def update_category(
    category_id: int,
    category: CategoryUpdate,
):
    """
    Update an existing category.
    """

    return await client.put(
        f"/categories/{category_id}",
        data=category.model_dump(exclude_none=True),
    )