import logging
from fastapi import FastAPI, Request
from mcp.server.sse import SseServerTransport
from mcp.server.fastmcp import FastMCP
from starlette.routing import Mount
from src.tools import tool_registry
from .resources import *

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MCP Server Running"}

@app.post("/")
async def post_root():
    return {"message": "MCP Server Running"}

sse_transport = SseServerTransport("/mcp/messages/")
app.router.routes.append(Mount("/mcp/messages", app=sse_transport.handle_post_message))

mcp = FastMCP()
for tool in tool_registry:
    mcp.tool()(tool)

@app.get("/mcp/sse")
async def handle_sse(request: Request):
    async with sse_transport.connect_sse(request.scope, request.receive, request._send) as (read_stream, write_stream):
        await mcp._mcp_server.run(
            read_stream,
            write_stream,
            mcp._mcp_server.create_initialization_options(),
        )
    return

app.get("/mcp")(handle_sse)

@app.post("/mcp/sse")
async def handle_sse_post(request: Request):
    return {"message": "SSE connections should use GET method"}

@app.get("/mcp/list_tools")
def list_tools():
    tools = []
    for func in tool_registry:
        tools.append({
            "name": func.__name__,
            "description": func.__doc__ or "",
            "parameters": list(func.__annotations__.items())
        })
    return tools

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)