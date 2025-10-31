from fastapi import FastAPI, HTTPException, Security, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging

# Import your agent and models
from app.trip_planner.agent import root_agent
from app.schemas.request_models import TripRequest
from app.schemas.response_models import TripResponse

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


@app.post("/plan_trip", response_model=TripResponse, tags=["trip_planning"])
async def plan_trip(trip_request: TripRequest):
    """
    Endpoint to plan a trip based on a user prompt.
    """
    logger.info(f"Received trip planning request: {trip_request.user_prompt}")
    try:
        # Run the agent
        trip_plan = root_agent.run(trip_request.user_prompt)

        # Create the response
        response = TripResponse(trip_plan=trip_plan)
        logger.info(f"Trip planning successful. Returning response.")
        return response

    except Exception as e:
        logger.exception("An error occurred during trip planning.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

# Example endpoint with authentication (if you need it)
# @app.get("/protected_resource", tags=["protected"])
# async def protected_resource(user_id: str = Depends(get_current_user_id)):
#     logger.info(f"Protected resource accessed by user: {user_id}")
#     return {"message": f"This is a protected resource for user {user_id}"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)