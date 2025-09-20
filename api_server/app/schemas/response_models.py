from pydantic import BaseModel
from typing import Dict, Any, Optional
from fastapi import status

class StandardResponse(BaseModel):
    data: Optional[Dict[str, Any]] = None
    status_code: int = status.HTTP_200_OK
    status_message: str = "Success"
