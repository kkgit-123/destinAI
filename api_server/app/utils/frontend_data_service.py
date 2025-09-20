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
    "displayText": 'Kerla cousin trip',
    "promptText": 'create me a itenary plan for my trip to kerla from Pune , I am travelling with my cousins . can you plan me a trip using all public transport options available . I am lanning to visit kerla from 2 october to 10 October , I want to have a bit of religious and party theme , also want to enjoy sunrises and elephants ',
  },
  {
    "id": 3,
    "displayText": 'Shimla trip',
    "promptText": 'can you plan me a trip to shimla from pune , consider that i am travlling wiht 4 others and i want to use public transportation as much as possible and my overall budget perhead is 10000 and want to have 5 days trip',
  },
  {
    "id": 4,
    "displayText": 'Road Trip to Rajasthan in Hindi',
    "promptText": 'provide me a itenary in hindi for a car road trip to rajasthan for 5 days from Surat , I am planning to go from 22 October to 30 october 2025 , I have a budget of 15000 per head and am travelling with my 4 friends in my hilux',
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
      return "3"
    elif "shimla" in prompt:
      return "4"
    elif "rajasthan" in prompt:
      return "1"
    elif "kerla" in prompt:
      return "2"
    else :
       return "5"
