from app.mcp_server import mcp


@mcp.resource("commerce://overview")
def commerce_overview() -> str:
    """
    Provides an overview of the Commerce domain.
    """

    return """
Enterprise Commerce Domain
==========================

Customers
---------
Customer master information.

Products
--------
Products available for sale.

Categories
----------
Product categories.

Orders
------
Customer orders and order details.

Employees
---------
Employees associated with the organization.

Suppliers
---------
Product suppliers.

Shippers
--------
Shipping providers.

Sales
-----
Sales and order-related business information.
"""


@mcp.resource("commerce://api-endpoints")
def commerce_api_endpoints() -> str:
    """
    Provides a high-level list of commerce API capabilities.
    """

    return """
Commerce API Capabilities
=========================

Customers
- Get customers
- Get customer by ID

Products
- Get products
- Get product by ID

Categories
- Get categories
- Get category by ID

Orders
- Get orders
- Get order by ID

Employees
- Get employees
- Get employee by ID

Suppliers
- Get suppliers
- Get supplier by ID

Shippers
- Get shippers
- Get shipper by ID

Sales
- Get sales information
"""