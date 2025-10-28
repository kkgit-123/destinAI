"""Inventory_agent for generating trip packing lists"""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from . import prompt

MODEL = "gemini-2.5-pro"

inventory_agent = Agent(
    model=LiteLlm(MODEL),
    name="inventory_agent",
    description="Creates a personalized packing list for the trip",
    instruction=prompt.INVENTORY_AGENT_PROMPT,
)
