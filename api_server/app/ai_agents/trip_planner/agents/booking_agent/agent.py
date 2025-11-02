from google.adk.agents import Agent
from google.adk.tools import google_search

from . import prompt

booking_agent = Agent(
    name="booking_agent",
    model="gemini-2.5-flash",
    instruction=prompt.BOOKING_AGENT_PROMPT,
    description="Intelligent agent to search and recommend hotels for travel planning using Google Search capabilities.",
    tools=[google_search],
    output_key="booking_details"
)

