from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.utils.frontend_data_service import get_plan_data, get_prompt_cards_data, get_trip_data, get_unified_trip_data, get_trip_cards_data

router = APIRouter()

@router.get("/plan-data", response_model=Dict[str, Any])
async def get_plan_data_api():
    """
    Returns dummy plan data.
    """
    return get_plan_data()

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
