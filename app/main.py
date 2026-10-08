import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from app.mcp_server import mcp

# Import server so that all tools, resources
# and prompts are registered.
import app.server


if __name__ == "__main__":
    mcp.run(transport="streamable-http")