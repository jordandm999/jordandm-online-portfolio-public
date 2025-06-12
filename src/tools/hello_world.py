import json
import yaml
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def hello_world() -> str:
    """
    A simple tool that returns "Hello, world!"
    """
    return "Hello, world!"