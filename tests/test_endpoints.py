import pytest
from httpx import AsyncClient
from src.website.website.asgi import application  # Adjust import if needed

@pytest.mark.asyncio
async def test_api_test():
    async with AsyncClient(app=application, base_url="http://testserver") as ac:
        response = await ac.get("/api/test")
        assert response.status_code == 200
        assert response.json() == {"message": "FastAPI is working!"}

@pytest.mark.asyncio
async def test_list_tools():
    async with AsyncClient(app=application, base_url="http://testserver") as ac:
        response = await ac.get("/api/mcp_server/list_tools")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_mcp_server_post():
    async with AsyncClient(app=application, base_url="http://testserver") as ac:
        response = await ac.post("/api/mcp_server", json={})
        # Adjust the expected status code and response as needed
        assert response.status_code in (200, 202, 400, 404)

# Add more tests for other endpoints as needed