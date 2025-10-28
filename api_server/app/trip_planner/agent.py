from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.planner_agent import planner_agent
from .sub_agents.inventory_agent import inventory_agent

MODEL = "gemini-2.5-pro"  # Use your preferred model version

root_agent = Agent(
    name="trip_coordinator",
    model=MODEL,
    description=(
        "Plans a user's entire trip by delegating creation of detailed itineraries "
        "and packing lists. Coordinates with specialized planning and inventory agents."
    ),
    instruction=prompt.TRIP_COORDINATOR_PROMPT,
    sub_agents=[planner_agent, inventory_agent],
    tools=[
        AgentTool(planner_agent),
        AgentTool(inventory_agent),
    ],
    output_key="trip_plan",
)
