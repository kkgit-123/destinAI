import time # Import the time module
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.utils.data import unified_trip_data,trip_cards_data

# Dummy data from ui-server/src/constants/promptCards.js
prompt_cards_data = [
  {
    "id": 1,
    "displayText": 'Kokan boys trip',
    "promptText": 'Plan me a trip for kokan boys only trip from Pune . its a trip for 10 days , and budget is aprox 20000 per person . and can you arrange me cab and bus for the transportationI want to start at 20 septemeber 2025',
  },
  {
    "id": 2,
    "displayText": 'Rajasthan Road trip',
    "promptText": 'Organize an adventure trip to the Amazon rainforest, focusing on eco-tourism, wildlife viewing, and local cultural experiences.',
  },
  {
    "id": 3,
    "displayText": 'Shimla trip',
    "promptText": 'can you plan me a trip to shimla from pune , consider that i am travlling wiht 4 others and i want to use public transportation as much as possible and my overall budget perhead is 10000 and want to have 5 days trip',
  },
  {
    "id": 4,
    "displayText": 'Hindi',
    "promptText": 'Create a solo backpacking itinerary through Southeast Asia for one month, covering budget-friendly options and must-see destinations.',
  },
]
def generate_travel_plan(id):
    return get_plan_data(id)

def get_plan_data(id: str) -> Dict[str, Any]:
    return unified_trip_data[int(id)-1]
    # return plan_data[0]

def get_prompt_cards_data() -> List[Dict[str, Any]]:
    return prompt_cards_data

def get_trip_data(id: str) -> Dict[str, Any]:
    return unified_trip_data[int(id)-1]
    # return trip_data

def get_unified_trip_data() -> Dict[str, Any]:
    return unified_trip_data


def get_trip_cards_data() -> List[Dict[str, Any]]:
    return trip_cards_data

def process_prompt(prompt):
    time.sleep(20) # Add a 5-second delay
    if "kokan" in prompt:
      return "1"
    elif "shimla" in prompt:
      return "3"
    elif "rajasthan" in prompt:
      return "2"
    elif "hindi" in prompt:
      return 4
    else :
       return 5
