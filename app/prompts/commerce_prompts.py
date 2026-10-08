from app.mcp_server import mcp


@mcp.prompt()
def customer_analysis(customer_id: str) -> str:

    return f"""
Analyze customer {customer_id}.

Please:

1. Retrieve the customer information.
2. Retrieve the customer's orders.
3. Summarize the customer's purchasing activity.
4. Identify frequently purchased products.
5. Identify order trends.
6. Highlight any unusual purchasing behavior.

Customer ID:
{customer_id}

Provide the result in a clear business-friendly format.
"""


@mcp.prompt()
def product_analysis(product_id: str) -> str:

    return f"""
Analyze product {product_id}.

Please:

1. Retrieve product information.
2. Identify the product category.
3. Identify the supplier.
4. Review relevant order information.
5. Summarize product demand.
6. Provide useful business observations.

Product ID:
{product_id}
"""


@mcp.prompt()
def sales_analysis() -> str:

    return """
Perform an enterprise sales analysis.

Please:

1. Retrieve available sales information.
2. Identify important sales trends.
3. Identify high-performing products.
4. Identify important customers.
5. Identify potential anomalies.
6. Summarize the findings.

Present the result as:

Executive Summary
-----------------
Key Trends
----------
Top Products
------------
Top Customers
-------------
Potential Issues
----------------
Recommendations
---------------
"""