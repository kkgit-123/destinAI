import uvicorn
from app.main import app
from logger import setup_logging
from app.config import get_config
import logging

# Setup logging
logger = setup_logging()
config = get_config()

if __name__ == "__main__":
    host = config.get("APP", "HOST", "0.0.0.0")
    port = config.getint("APP", "PORT", 8000)
    logger.info(f"Starting FastAPI application with Uvicorn on {host}:{port}.")
    uvicorn.run(app, host=host, port=port)
