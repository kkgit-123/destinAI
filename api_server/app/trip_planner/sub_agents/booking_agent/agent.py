from google.adk.agents import Agent
from google.adk.tools import google_search

booking_agent = Agent(
    name="booking_agent",
    model="gemini-2.5-flash",
    instruction=(
        """You are a hotel recommendation assistant. 
        Suggest relevant hotels for trips in the user-specified location.
        
        Here is the input from user:
        Destination: {formatted_trip_inputs.destination}
        Start Date: {formatted_trip_inputs.start_date}
        End Date: {formatted_trip_inputs.end_date}
        Budget: {formatted_trip_inputs.budget}

        If the request includes preferences like budget, rating, or amenities, 
        take those into account. List hotel names, ratings, addresses, and unique features. 
        Always present 2-3 of the most relevant hotels, cite your sources, and ask for missing details if needed."""
    ),
    description="Intelligent agent to search and recommend hotels for travel planning using Google Search capabilities.",
    tools=[google_search],
    output_key="booking_details"
)
