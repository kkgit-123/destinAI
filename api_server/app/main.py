from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api import dummy_api, employee_api, frontend_api
from logger import setup_logging
from app.helper.exception_handlers import http_exception_handler, unhandled_exception_handler
from app.helper.auth import get_current_user_id
import logging

# Setup logging
logger = setup_logging()

app = FastAPI(
    title="FastAPI Boilerplate",
    description="A boilerplate for a fast and standardized FastAPI application.",
    version="1.0.0",
    # dependencies=[Security(get_current_user_id)] # Apply authentication globally if needed for all endpoints
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include API routers
app.include_router(dummy_api.router, prefix="", tags=["dummy"])
app.include_router(employee_api.router, prefix="", tags=["employees"])
app.include_router(frontend_api.router, prefix="/frontend", tags=["frontend"])

# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

from app.storage.database import initialize_database

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup event triggered.")
    initialize_database()
    logger.info("Database initialized and checked for dummy data.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown event triggered.")

@app.get("/", tags=["root"])
async def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the FastAPI Boilerplate!"}
