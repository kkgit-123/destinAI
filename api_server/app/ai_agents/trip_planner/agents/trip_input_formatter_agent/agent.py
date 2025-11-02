from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro"


trip_input_formatter_agent = LlmAgent(
    name="trip_input_formatter_agent",
    model=MODEL,
    instruction=prompt.INPUT_FORMATTER_AGENT_PROMPT,
    description="Extracts structured trip details for agent pipeline.",
    output_key="formatted_trip_inputs"
)

