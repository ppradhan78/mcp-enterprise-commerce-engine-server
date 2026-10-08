from typing import Any

from app.clients.northwind_client import NorthwindClient
from app.mcp_server import mcp


client = NorthwindClient()

@mcp.tool()
async def get_sales_summary() -> dict[str, Any]:
    """
    Get a basic sales summary based on Northwind orders.
    """

    orders =  await client.get(
        "/Orders"
    )

    if not isinstance(orders, list):
        return {
            "orders": orders
        }

    total_orders = len(orders)

    total_freight = 0.0

    for order in orders:

        freight = order.get(
            "freight",
            0
        )

        try:
            total_freight += float(
                freight or 0
            )
        except (TypeError, ValueError):
            pass

    return {
        "total_orders": total_orders,
        "total_freight": total_freight,
    }

@mcp.tool()
async def get_customer_sales(
    customer_id: str,
) -> dict[str, Any]:
    """
    Get sales information for a customer.
    """

    orders =  await client.get(
        "/Orders"
    )

    if not isinstance(orders, list):
        return {
            "customer_id": customer_id,
            "orders": orders,
        }

    customer_orders = [
        order
        for order in orders
        if order.get("customerId")
        == customer_id
    ]

    total_freight = 0.0

    for order in customer_orders:

        try:
            total_freight += float(
                order.get("freight", 0) or 0
            )
        except (TypeError, ValueError):
            pass

    return {
        "customer_id": customer_id,
        "order_count": len(customer_orders),
        "total_freight": total_freight,
        "orders": customer_orders,
    }

@mcp.tool()
async def get_employee_sales(
    employee_id: int,
) -> dict[str, Any]:
    """
    Get sales information for an employee.
    """

    orders =  await client.get(
        "/Orders"
    )

    if not isinstance(orders, list):
        return {
            "employee_id": employee_id,
            "orders": orders,
        }

    employee_orders = [
        order
        for order in orders
        if order.get("employeeId")
        == employee_id
    ]

    return {
        "employee_id": employee_id,
        "order_count": len(employee_orders),
        "orders": employee_orders,
    }