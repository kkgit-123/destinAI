from fastapi import FastAPI, HTTPException, Security, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging

# Import your agent and models
from app.trip_planner.agent import trip_pipeline_agent
from app.schemas.request_models import TripRequest
from app.schemas.response_models import StandardResponse
# from google.adk.runners import Runner  # Removed google.adk dependency
# from google.adk.agents.invocation_context import InvocationContext  # Removed google.adk dependency

# Import helper functions (if you have any)
from app.helper.exception_handlers import http_exception_handler, unhandled_exception_handler
from app.helper.auth import get_current_user_id  # Example auth function

# Import database initialization (if needed)
from app.storage.database import initialize_database

# Import logging setup
from logger import setup_logging

# Initialize logging
logger = setup_logging()

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Trip Planner API",
    description="An API for planning trips using an agentic workflow.",
    version="1.0.0",
    # dependencies=[Security(get_current_user_id)] # Example: Apply authentication globally
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - adjust for production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


@app.on_event("startup")
async def startup_event():
    logger.info("Application startup event triggered.")
    initialize_database()  # Initialize database (if you are using one)
    logger.info("Database initialized.")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown event triggered.")


@app.get("/", tags=["root"])
async def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the Trip Planner API!"}


# (Other code remains the same as above, only the run_trip_pipeline function changes)

@app.post("/run_trip_pipeline")
async def run_trip_pipeline(request: TripRequest):
    logger.info(f"Received external request: {request.query}")

    try:
        # Run agentic workflow
        result = await trip_pipeline_agent.run_async(request.query)  # Assuming 'run' is async
        logger.info("TripPipelineAgent workflow executed successfully.")
        return {"result": result}
    except Exception as exc:
        logger.error(f"Workflow execution error: {exc}")
        return {"error": str(exc)}