"""Planner_agent for building trip itineraries"""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from . import prompt
import os
from dotenv import load_dotenv

load_dotenv()

# api_key = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-2.5-pro"

planner_agent = Agent(
    model=MODEL,
    name="planner_agent",
    description="Builds an itinerary (dates, destination, budget)",
    instruction=prompt.PLANNER_AGENT_PROMPT,
    output_key="trip_plan"
)
