from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.utils.frontend_data_service import get_plan_data, get_prompt_cards_data, get_trip_data, get_unified_trip_data, get_trip_cards_data
from app.gemini.get_response import generate_travel_plan

router = APIRouter()

@router.get("/plan-data", response_model=Dict[str, Any])
async def get_plan_data_api(user_message: str):
    """
    Generates a travel plan from a pick-up spot to a destination using an LLM.
    """
    try:
        plan_content = generate_travel_plan(user_message)
        return {"plan": plan_content}
    except ValueError as ve:  # Catch specific ValueError from llm_service
        raise HTTPException(status_code=400, detail=str(ve))  # Client error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")  # Server error

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

@router.get("/trip-data", response_model=Dict[str, Any])
async def get_trip_data_api():
    """
    Returns dummy trip data.
    """
    return get_trip_data()

@router.get("/unified-trip-data", response_model=Dict[str, Any])
async def get_unified_trip_data_api():
    """
    Returns dummy unified trip data.
    """
    return get_unified_trip_data()
