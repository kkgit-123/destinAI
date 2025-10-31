from pydantic import BaseModel

# class TripRequest(BaseModel):
#     # destination: str
#     # start_date: str
#     # end_date: str
#     # budget: float
#     user_prompt: str

class TripRequest(BaseModel):
    query: str
