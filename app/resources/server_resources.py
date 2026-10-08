from app.mcp_server import mcp
from app.config import configuration


@mcp.resource("server://info")
def server_info() -> str:

    return f"""
MCP Server Information
======================

Name:
{configuration.mcp_server_name}

Purpose:
Enterprise Commerce MCP Server

Domain:
Northwind Commerce

Capabilities:
- Customer information
- Product information
- Order information
- Supplier information
- Employee information
- Category information
- Shipper information
- Sales information
- Weather information

Architecture:

AI Client
    |
    v
MCP Client
    |
    v
Enterprise Commerce MCP Server
    |
    +-- Tools
    |
    +-- Resources
    |
    +-- Prompts
    |
    +-- Northwind API
    |
    +-- Weather API
"""