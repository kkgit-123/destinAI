from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.utils.frontend_data_service import process_prompt,get_plan_data, get_prompt_cards_data, get_trip_data, get_unified_trip_data, get_trip_cards_data
from app.schemas.request_models import PromptRequest
from app.schemas.response_models import StandardResponse

router = APIRouter()

@router.get("/plan-data/{id}", response_model=Dict[str, Any])
async def get_plan_data_api(id: str):
    """
    Returns dummy plan data based on ID.
    """
    return get_plan_data(id)

@router.get("/trip-cards", response_model=List[Dict[str, Any]])
async def get_trip_cards_api():
    """
    Returns dummy trip cards data.
    """
    return get_trip_cards_data()

@router.get("/prompt-cards", response_model=List[Dict[str, Any]])
async def get_prompt_cards_api():
    """
    Returns dummy prompt cards data.
    """
    return get_prompt_cards_data()

@router.get("/trip-data/{id}", response_model=Dict[str, Any])
async def get_trip_data_api(id: str):
    """
    Returns dummy trip data based on ID.
    """
    return get_trip_data(id)

@router.get("/unified-trip-data", response_model=Dict[str, Any])
async def get_unified_trip_data_api():
    """
    Returns dummy unified trip data.
    """
    return get_unified_trip_data()

@router.post("/process-prompt", response_model=StandardResponse)
async def process_prompt_api(request: PromptRequest):
    """
    Processes the prompt and returns a plan ID.
    """
    print(request.prompt)
    result=process_prompt(request.prompt)
    return StandardResponse(data={"id": result})
