from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def hello_world() -> str:
    """
    A simple test tool that returns a greeting
    """
    return "Hello from MCP Server!"