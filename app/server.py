from mcp.server.fastmcp import FastMCP

from app.config import configuration
from app.clients.northwind_client import NorthwindClient

from app.tools.customers import (
    get_customers,
    search_customers,
)



from app.tools.products import (
    get_products,
    search_products,
    get_products_by_category,
)

from app.tools.orders import (
    get_orders,
    get_orders_by_customer,
    get_orders_by_employee,
)

from app.tools.employees import (
    get_employees,
    search_employees,
)

from app.tools.categories import (
    get_categories,
    search_categories,
)

from app.tools.suppliers import (
    get_suppliers,
    search_suppliers,
)

from app.tools.shippers import (
    get_shippers,
    search_shippers,
)

from app.tools.shippers import (
    get_shippers,
    search_shippers,
)

from app.tools.sales import (
    get_sales_summary,
    get_customer_sales,
    get_employee_sales,
)


mcp = FastMCP(
    configuration.settings.mcp_server_name
)


# ---------------------------------------------------------
# Customer Tools
# ---------------------------------------------------------

@mcp.tool()
async def customers(
    customer_id: str | None = None,
):
    """
    Retrieve Northwind customers.

    Provide customer_id to retrieve one customer.
    Leave empty to retrieve all customers.
    """

    return await get_customers(
        customer_id
    )


@mcp.tool()
async def customer_search(
    search: str,
):
    """
    Search Northwind customers.
    """

    return await search_customers(
        search
    )


# ---------------------------------------------------------
# Product Tools
# ---------------------------------------------------------

@mcp.tool()
async def products(
    product_id: int | None = None,
):
    """
    Retrieve Northwind products.

    Provide product_id to retrieve one product.
    """

    return await get_products(
        product_id
    )


@mcp.tool()
async def product_search(
    search: str,
):
    """
    Search Northwind products.
    """

    return await search_products(
        search
    )


@mcp.tool()
async def products_by_category(
    category_id: int,
):
    """
    Retrieve products belonging to a category.
    """

    return await get_products_by_category(
        category_id
    )


# ---------------------------------------------------------
# Order Tools
# ---------------------------------------------------------

@mcp.tool()
async def orders(
    order_id: int | None = None,
):
    """
    Retrieve Northwind orders.
    """

    return await get_orders(
        order_id
    )


@mcp.tool()
async def orders_by_customer(
    customer_id: str,
):
    """
    Retrieve orders for a customer.
    """

    return await get_orders_by_customer(
        customer_id
    )


@mcp.tool()
async def orders_by_employee(
    employee_id: int,
):
    """
    Retrieve orders handled by an employee.
    """

    return await get_orders_by_employee(
        employee_id
    )


# ---------------------------------------------------------
# Employee Tools
# ---------------------------------------------------------

@mcp.tool()
async def employees(
    employee_id: int | None = None,
):
    """
    Retrieve Northwind employees.
    """

    return await get_employees(
        employee_id
    )


@mcp.tool()
async def employee_search(
    search: str,
):
    """
    Search Northwind employees.
    """

    return await search_employees(
        search
    )


# ---------------------------------------------------------
# Category Tools
# ---------------------------------------------------------

@mcp.tool()
async def categories(
    category_id: int | None = None,
):
    """
    Retrieve Northwind categories.
    """

    return await get_categories(
        category_id
    )


@mcp.tool()
async def category_search(
    search: str,
):
    """
    Search Northwind categories.
    """

    return await search_categories(
        search
    )


# ---------------------------------------------------------
# Supplier Tools
# ---------------------------------------------------------

@mcp.tool()
async def suppliers(
    supplier_id: int | None = None,
):
    """
    Retrieve Northwind suppliers.
    """

    return await get_suppliers(
        supplier_id
    )


@mcp.tool()
async def supplier_search(
    search: str,
):
    """
    Search Northwind suppliers.
    """

    return await search_suppliers(
        search
    )


# ---------------------------------------------------------
# Shipper Tools
# ---------------------------------------------------------

@mcp.tool()
async def shippers(
    shipper_id: int | None = None,
):
    """
    Retrieve Northwind shippers.
    """

    return await get_shippers(
        shipper_id
    )


@mcp.tool()
async def shipper_search(
    search: str,
):
    """
    Search Northwind shippers.
    """

    return await search_shippers(
        search
    )


# ---------------------------------------------------------
# Sales Tools
# ---------------------------------------------------------

@mcp.tool()
async def sales_summary():
    """
    Get an overall Northwind sales summary.
    """

    return await get_sales_summary()


@mcp.tool()
async def customer_sales(
    customer_id: str,
):
    """
    Get sales information for a customer.
    """

    return await get_customer_sales(
        customer_id
    )


@mcp.tool()
async def employee_sales(
    employee_id: int,
):
    """
    Get sales information for an employee.
    """

    return await get_employee_sales(
        employee_id
    )


# ---------------------------------------------------------
# Health Tool
# ---------------------------------------------------------

@mcp.tool()
async def northwind_health():
    """
    Check connectivity to the Northwind API.
    """

    client = NorthwindClient()

    return await client.health_check()


# ---------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    mcp.run()