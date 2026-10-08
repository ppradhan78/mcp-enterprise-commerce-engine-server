from typing import Any, Optional

from app.clients.northwind_client import NorthwindClient
from app.mcp_server import mcp


client = NorthwindClient()

@mcp.tool()
async def get_employees(
    employee_id: Optional[int] = None,
) -> Any:
    """
    Get employees.

    If employee_id is provided, return one employee.
    Otherwise return all employees.
    """

    if employee_id is not None:

        return  client.get(
            f"/Employees/{employee_id}"
        )

    return  client.get(
        "/Employees"
    )

@mcp.tool()
async def search_employees(
    search: str,
) -> Any:
    """
    Search employees.
    """

    employees =  client.get(
        "/Employees"
    )

    if not isinstance(employees, list):
        return employees

    search_lower = search.lower()

    return [
        employee
        for employee in employees
        if search_lower in str(employee).lower()
    ]