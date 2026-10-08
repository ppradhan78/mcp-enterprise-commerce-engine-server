# MCP Enterprise Commerce Engine Server

An enterprise-style Model Context Protocol (MCP) server that exposes
Northwind Commerce REST APIs as MCP tools.

The server allows an AI application or MCP client to interact with
customers, products, orders, employees, categories, suppliers,
shippers and sales information.

---

## Architecture

```text
                    AI Application
                          |
                          |
                    MCP Client
                          |
                          |
                MCP Enterprise Server
                          |
        +-----------------+-----------------+
        |                 |                 |
    Customers         Products           Orders
        |                 |                 |
    Employees         Categories        Suppliers
        |                 |                 |
    Shippers             Sales
        |                 |                 |
        +-----------------+-----------------+
                          |
                          |
                 Northwind Client
                          |
                          |
                 Northwind REST API