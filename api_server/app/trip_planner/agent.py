from .sub_agents.trip_input_formatter_agent import trip_input_formatter_agent
from .sub_agents.planner_agent import planner_agent
from .sub_agents.itinerary_agent import itinerary_agent
from .sub_agents.output_formatter_agent import output_formatter_agent
from dotenv import load_dotenv
from google.adk.agents import SequentialAgent


load_dotenv()

MODEL = "gemini-2.5-pro" 

trip_pipeline_agent = SequentialAgent(
    name="TripPipelineAgent",
    sub_agents=[
        trip_input_formatter_agent,  
        planner_agent,               
        itinerary_agent,              
        output_formatter_agent
    ],
    description="Parses user prompt, builds trip plan, and generates itinerary."
)

root_agent = trip_pipeline_agent
