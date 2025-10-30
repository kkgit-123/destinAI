"""Inventory_agent for generating trip packing lists"""

from google.adk.agents import LlmAgent

from . import prompt
from dotenv import load_dotenv

load_dotenv()
MODEL = "gemini-2.5-pro"

itinerary_agent = LlmAgent(
    name="itinerary_agent",
    model=MODEL,
    instruction=prompt.INVENTORY_AGENT_PROMPT,
    description="Creates a personalized packing list for the trip",
    output_key="iternary"
)
