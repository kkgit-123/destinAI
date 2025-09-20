from fastapi import APIRouter, HTTPException, status
from app.schemas.response_models import StandardResponse
from typing import List, Dict, Any
from fastapi import Depends
from . import employee_service

router = APIRouter()

from app.helper.auth import get_current_user_id

@router.get("/employees", response_model=StandardResponse)
async def get_employees(user_id: int = Depends(get_current_user_id)):
    """
    A dummy API endpoint to get a list of employees with a standardized response.
    """
    employees = employee_service.get_all_employees(user_id)
    return StandardResponse(data={"employees": employees, "accessed_by_user": user_id}, status_code=status.HTTP_200_OK, status_message="Employees retrieved successfully")

@router.get("/employees/{employee_id}", response_model=StandardResponse)
async def get_employee_by_id(employee_id: int, user_id: int = Depends(get_current_user_id)):
    """
    A dummy API endpoint to get a single employee by ID with a standardized response.
    """
    employee = employee_service.get_employee_by_id(employee_id, user_id)
    if employee:
        return StandardResponse(data={"employee": employee, "accessed_by_user": user_id}, status_code=status.HTTP_200_OK, status_message="Employee retrieved successfully")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
