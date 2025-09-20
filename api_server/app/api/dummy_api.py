from fastapi import APIRouter, HTTPException, status
from app.schemas.response_models import StandardResponse
from app.schemas.request_models import DummyItem
from typing import Dict, Any, Optional

from fastapi import Depends

router = APIRouter()

from app.helper.auth import get_current_user_id

@router.get("/dummy", response_model=StandardResponse)
async def read_dummy_item(user_id: int = Depends(get_current_user_id)):
    """
    A dummy API endpoint that returns a simple message with a standardized response.
    """
    response_data = {"message": f"Hello from dummy API for user {user_id}!"}
    return StandardResponse(data=response_data, status_code=status.HTTP_200_OK, status_message="Dummy item retrieved successfully")

@router.post("/dummy", response_model=StandardResponse)
async def create_dummy_item(item: DummyItem, user_id: int = Depends(get_current_user_id)):
    """
    A dummy API endpoint that accepts a POST request with a DummyItem and returns a standardized response.
    """
    response_data = {"received_name": item.name, "received_value": item.value, "user_id": user_id}
    return StandardResponse(data=response_data, status_code=status.HTTP_201_CREATED, status_message="Dummy item created successfully")
