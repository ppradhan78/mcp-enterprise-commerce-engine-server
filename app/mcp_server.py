from mcp.server.fastmcp import FastMCP

from app.config import settings


mcp = FastMCP(
    settings.mcp_server_name
)