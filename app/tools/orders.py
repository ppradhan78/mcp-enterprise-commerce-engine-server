from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient


client = NorthwindClient()


async def get_orders(
    order_id: Optional[int] = None,
) -> Any:
    """
    Get orders.

    If order_id is provided, return one order.
    Otherwise return all orders.
    """

    if order_id is not None:

        return await client.get(
            f"/Orders/{order_id}"
        )

    return await client.get(
        "/Orders"
    )


async def get_orders_by_customer(
    customer_id: str,
) -> Any:
    """
    Get orders for a specific customer.
    """

    orders = await client.get(
        "/Orders"
    )

    if not isinstance(orders, list):
        return orders

    return [
        order
        for order in orders
        if (
            order.get("customerId")
            == customer_id
        )
    ]


async def get_orders_by_employee(
    employee_id: int,
) -> Any:
    """
    Get orders handled by an employee.
    """

    orders = await client.get(
        "/Orders"
    )

    if not isinstance(orders, list):
        return orders

    return [
        order
        for order in orders
        if (
            order.get("employeeId")
            == employee_id
        )
    ]