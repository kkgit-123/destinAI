from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.response_models import StandardResponse
from logger import setup_logging

logger = setup_logging()

async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handles FastAPI's HTTPException and returns a standardized error response.
    """
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=StandardResponse(
            status_code=exc.status_code,
            status_message=exc.detail,
            data=None
        ).model_dump()
    )

async def unhandled_exception_handler(request: Request, exc: Exception):
    """
    Handles all unhandled exceptions and returns a standardized error response.
    """
    logger.exception(f"Unhandled Exception: {exc}") # Log the full traceback
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=StandardResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            status_message="An unexpected error occurred.",
            data=None
        ).model_dump()
    )
