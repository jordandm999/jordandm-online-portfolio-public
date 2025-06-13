"""
ASGI config for website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

# Get the Django ASGI application
django_app = get_asgi_application()

# Create a FastAPI application that will be the main ASGI app
app = FastAPI()

# Add CORS middleware if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add a test FastAPI route
@app.get("/api/test")
async def test_endpoint():
    return {"message": "FastAPI is working!"}

# Create a middleware that will handle both FastAPI and Django requests
async def django_middleware(scope, receive, send):
    if scope["type"] == "http":
        # Let FastAPI handle /api/ routes
        if scope["path"].startswith("/api/"):
            await app(scope, receive, send)
        else:
            # Pass all other requests to Django
            await django_app(scope, receive, send)
    else:
        # For other types of requests (like websocket), pass to Django
        await django_app(scope, receive, send)

# This is what uvicorn will use
application = django_middleware
