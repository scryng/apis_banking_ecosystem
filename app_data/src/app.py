import uvicorn
from fastapi import FastAPI

from src.config import settings
from src.routes import router

app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description,
)
"""
Creates a FastAPI application using settings loaded from the config module.

Attributes:
    title (str): Title of the API.
    version (str): Version of the API.
    description (str): Description of the API.
"""

app.include_router(router)
"""
Includes the routes defined in the imported router from `routes.py`.
"""

if __name__ == '__main__':
    """
    Checks if the script is being run directly (not imported as a module).
    Starts the Uvicorn server with the FastAPI application.
    Args:
        host (str): Host defined in the settings;
        port (int): Port defined in the settings.
    """
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)
