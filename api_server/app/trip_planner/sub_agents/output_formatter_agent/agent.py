from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro"

output_formatter_agent = LlmAgent(
    name="output_formatter_agent",
    model=MODEL,
    instruction=prompt.OUTPUT_FORMATTER_AGENT_PROMPT,
    description="Extracts structured trip details for agent pipeline.",
    output_key="formatted_trip_inputs"
)

