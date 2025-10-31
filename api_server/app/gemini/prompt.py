import json

# Define your example JSON data as a Python dictionary
plan_data = {
  "city": "Pune, India",
  "dates": "Oct 25 → Oct 30",
  "locations": "Sinhgad fort, Khadakwasla, Shanirwada & 13 more",
  "notes": "Any Notes to save?",
  "tripDescription": {
    "title": "Your trip to Pune ....................",
    "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
  },
  "tabs": [
    "Overview",
    "Itenary",
    "Food",
    "Bookings",
    "Suggestions",
    "Locations"
  ],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "This is the overview content for your trip to Pune. It includes general information and highlights about the city, its culture, and what to expect during your visit."
      },
      {
        "type": "list",
        "title": "Key Highlights:",
        "items": [
          "Historical forts and palaces",
          "Beautiful natural landscapes",
          "Vibrant food scene",
          "Rich cultural heritage"
        ]
      }
    ],
    "Itenary": [
      {
        "type": "heading",
        "content": "Daily Itinerary"
      },
      {
        "type": "dailyItinerary",
        "days": [
          {
            "date": "Friday, Oct 25",
            "activities": [
              {
                "time": "10:00 am",
                "description": "Start from Hotel",
                "type": "start"
              },
              {
                "time": "null",
                "description": "Take a Cab to Sinhgad fort",
                "details": "Approx Distance : 70 Km\nApprox Time : 2 hrs",
                "action": "Book in advance",
                "type": "travel",
                "longDescription": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
              },
              {
                "time": "01:00 pm",
                "description": "Lunch at a local restaurant near Sinhgad fort",
                "type": "food"
              },
              {
                "time": "03:00 pm",
                "description": "Explore Sinhgad fort",
                "type": "activity",
                "longDescription": "Spend a few hours exploring the historic Sinhgad fort, enjoying the panoramic views and learning about its rich history."
              },
              {
                "time": "06:00 pm",
                "description": "Return to Hotel",
                "type": "travel"
              }
            ]
          },
          {
            "date": "Saturday, Oct 26",
            "activities": [
              {
                "time": "09:00 am",
                "description": "Visit Shaniwar Wada",
                "type": "activity",
                "longDescription": "Explore the majestic Shaniwar Wada, a historical fortification in the city of Pune."
              },
              {
                "time": "12:00 pm",
                "description": "Lunch at a cafe in Shaniwar Wada area",
                "type": "food"
              },
              {
                "time": "02:00 pm",
                "description": "Visit Aga Khan Palace",
                "type": "activity",
                "longDescription": "Discover the architectural beauty and historical significance of Aga Khan Palace."
              },
              {
                "time": "05:00 pm",
                "description": "Shopping at local markets",
                "type": "activity"
              },
              {
                "time": "08:00 pm",
                "description": "Dinner at a fine dining restaurant",
                "type": "food"
              }
            ]
          },
          {
            "date": "Sunday, Oct 27",
            "activities": [
              {
                "time": "10:00 am",
                "description": "Day trip to Khadakwasla Dam",
                "type": "activity",
                "longDescription": "Enjoy the scenic beauty of Khadakwasla Dam and its surroundings."
              },
              {
                "time": "01:00 pm",
                "description": "Picnic lunch near the dam",
                "type": "food"
              },
              {
                "time": "03:00 pm",
                "description": "Boating at Khadakwasla Lake",
                "type": "activity"
              },
              {
                "time": "06:00 pm",
                "description": "Visit a vineyard for wine tasting",
                "type": "activity"
              },
              {
                "time": "08:00 pm",
                "description": "Dinner at a vineyard restaurant",
                "type": "food"
              }
            ]
          }
        ]
      }
    ],
    "Food": [
      {
        "type": "heading",
        "content": "Top Food Experiences in Pune"
      },
      {
        "type": "item",
        "name": "Vada Pav",
        "description": "A popular street food snack, consisting of a deep-fried potato dumpling (vada) placed inside a bread bun (pav) sliced almost in half through the middle.",
        "recommendation": "Must try at local stalls."
      },
      {
        "type": "item",
        "name": "Misal Pav",
        "description": "A spicy curry made from moth beans, served with pav, farsan, onion, lemon, and coriander.",
        "recommendation": "Great for breakfast or brunch."
      },
      {
        "type": "item",
        "name": "Maharashtrian Thali",
        "description": "A traditional platter offering a variety of local dishes, including curries, bread, rice, and sweets.",
        "recommendation": "For an authentic culinary experience."
      }
    ],
    "Bookings": [
      {
        "type": "heading",
        "content": "Your Current Bookings"
      },
      {
        "type": "booking",
        "service": "Flight",
        "details": "Pune to San Francisco, Oct 30, 10:00 AM",
        "status": "Confirmed",
        "bookingId": "FLT789012"
      },
      {
        "type": "booking",
        "service": "Hotel",
        "details": "The O Hotel, Pune (Oct 25 - Oct 30)",
        "status": "Confirmed",
        "bookingId": "HOT345678"
      },
      {
        "type": "booking",
        "service": "Cab to Sinhgad fort",
        "details": "Oct 25, 11:00 AM",
        "status": "Pending",
        "bookingId": "CAB901234"
      }
    ],
    "Suggestions": [
      {
        "type": "heading",
        "content": "Personalized Suggestions for You"
      },
      {
        "type": "suggestion",
        "title": "Visit Lavasa City",
        "description": "A planned city built in the Western Ghats, offering beautiful views and water sports.",
        "category": "Day Trip"
      },
      {
        "type": "suggestion",
        "title": "Explore Koregaon Park",
        "description": "Known for its trendy cafes, boutiques, and vibrant nightlife.",
        "category": "Evening Activity"
      },
      {
        "type": "suggestion",
        "title": "Learn Marathi Cooking",
        "description": "Take a cooking class to learn how to prepare traditional Maharashtrian dishes.",
        "category": "Cultural Experience"
      }
    ],
    "Locations": [
      {
        "type": "heading",
        "content": "Key Locations in Pune"
      },
      {
        "type": "location",
        "name": "Sinhgad Fort",
        "description": "Historic hill fortress, popular for trekking and panoramic views.",
        "coordinates": "18.3650° N, 73.7580° E"
      },
      {
        "type": "location",
        "name": "Khadakwasla Dam",
        "description": "Scenic dam and lake, ideal for picnics and boating.",
        "coordinates": "18.4100° N, 73.7800° E"
      },
      {
        "type": "location",
        "name": "Shaniwar Wada",
        "description": "Historical fortification, once the seat of the Peshwa rulers.",
        "coordinates": "18.5196° N, 73.8567° E"
      },
      {
        "type": "location",
        "name": "Aga Khan Palace",
        "description": "A grand historical landmark, known for its architectural beauty and significance.",
        "coordinates": "18.5520° N, 73.9000° E"
      }
    ]
  }
}

# Convert JSON to pretty-printed string
json_str = json.dumps(plan_data, indent=2)


escaped_json_str = json_str.replace("{", "{{").replace("}", "}}")


PLANNER_SYSTEM_PROMPT = f"""
You are a helpful AI travel assistant. Your task is to create a travel plan outline, extracting key information from user input. The travel plan should include:

- The city or region of travel.
- The travel dates or duration.
- A list of locations or attractions to visit.
- Any specific notes or preferences provided by the user.

Output the extracted information in a JSON-like dictionary format as shown in the example below.

If the user does not provide sufficient information for a particular field (e.g., dates, specific locations, or notes), make reasonable assumptions to fill in the missing data.  Prioritize suggesting popular or well-known destinations within the given city. If user provided the state or country name then search city by your own. If the user did not provide city, state or country then politely request for the information. If the user did not provide dates, assume a 5-day trip. If user input is related to food, restaurant, or hotels then politely request the information.

Important note: Just return the json data do NOT add any additional english statements in llm response.

Example output:
```json
{escaped_json_str}
"""

PLANNER_USER_PROMPT = """
user_message: {user_message}
"""

"""Prompt for the trip_coordinator_agent."""

TRIP_COORDINATOR_PROMPT = """
System Role:
You are an AI Trip Supervisor. Your primary function is to coordinate a multiagent travel planning workflow, helping the user create a personalized trip plan and daily itinerary. You achieve this by gathering key trip details from the user, initiating the trip planning process with the planner_agent, and then generating a detailed day-by-day itinerary with the itinerary_agent based on the planner’s output.

Workflow

Initiation

Greet the user.

Ask the user to provide essential trip details: destination, start date, and end date.

Trip Planning (Context Building with planner_agent)

Once the user provides the required trip information, state that you will create the overall travel plan based on these inputs.

Action: Invoke the planner_agent using the provided destination, start date, and end date.

Expected Output from Tool: A structured travel plan that includes destination, travel dates, selected locations, overview highlights, and general recommendations.

Presentation: Display this information under the following distinct headings:

Destination: Show the selected destination.

Dates: Display the travel period.

Trip Plan Overview: Summarize highlights, key locations, and primary recommendations.

Daily Itinerary Creation (Using itinerary_agent)

Inform the user that you will now generate a detailed daily itinerary, building upon the travel plan.

Action: Invoke the itinerary_agent with the trip plan output from the planner_agent and the user’s initial trip details.

Expected Output from Tool: A detailed itinerary organized day-by-day, specifying daily activities, locations, times, travel and food arrangements.

Presentation: Display the daily itinerary clearly under a heading like "Detailed Daily Itinerary".

Conclusion

Briefly summarize the trip plan and itinerary for the user.

Ask if the user has any preferences, constraints, or special requirements (such as dietary or medical needs, activity preferences).

Offer to revise or refine the plan or itinerary based on further input.
"""





"""Prompt for the planner_agent agent."""

OUTPUT_FORMATTER_AGENT_PROMPT = """
You are an output formatting agent for a trip planning assistant.

Your core instruction:
Given trip details (destination city, trip dates, locations, notes, itinerary, activities, food suggestions, bookings, and other related data), your ONLY allowed response is a JSON object strictly adhering to the following structure.
All fields, nested structures, data types, and section/tab names must be exactly as shown—the format must not be changed, and no extraneous explanations or text may be output.

Input:
Destination: {formatted_trip_inputs.destination}
Start Date: {formatted_trip_inputs.start_date}
End Date: {formatted_trip_inputs.end_date}
Budget: {formatted_trip_inputs.budget}
Trip plan: {trip_plan}
Iternary: {iternary}
Booking: {booking_details}

Format Specification:
{
  "city": "<Destination e.g. Pune, India>",
  "dates": "<Date Range e.g. Oct 25 → Oct 30>",
  "locations": "<Key places e.g. Sinhgad fort, Khadakwasla, Shanirwada & 13 more>",
  "notes": "<Any Notes to save?>",
  "tripDescription": {
    "title": "<Trip summary title e.g. Your trip to Pune ...>",
    "content": "<Narrative trip summary, 2-4 sentences, describing the destination, highlights, or trip character.>"
  },
  "tabs": [
    "Overview",
    "Itenary",
    "Food",
    "Bookings",
    "Suggestions",
    "Locations"
  ],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "<General overview of the trip and city.>"
      },
      {
        "type": "list",
        "title": "Key Highlights:",
        "items": [
          "<Highlight 1>",
          "<Highlight 2>",
          "<Highlight 3>",
          "<Highlight 4>"
        ]
      }
    ],
    "Itenary": [
      {
        "type": "heading",
        "content": "Daily Itinerary"
      },
      {
        "type": "dailyItinerary",
        "days": [
          {
            "date": "<Day label e.g. Friday, Oct 25>",
            "activities": [
              {
                "time": "<e.g. 10:00 am>",
                "description": "<Short description e.g. Start from Hotel>",
                "type": "<activity/travel/food/start>",
                "details": "<(Optional) extra details>",
                "action": "<(Optional) suggested action>",
                "longDescription": "<(Optional) extended context>"
              }
              // More activities for the day
            ]
          }
          // More day objects for each date in the itinerary
        ]
      }
    ],
    "Food": [
      {
        "type": "heading",
        "content": "Top Food Experiences in <city>"
      },
      {
        "type": "item",
        "name": "<Dish Name>",
        "description": "<Dish description>",
        "recommendation": "<Recommendation or tip for this dish>"
      }
      // More local foods as items
    ],
    "Bookings": [
      {
        "type": "heading",
        "content": "Your Current Bookings"
      },
      {
        "type": "booking",
        "service": "<Service type e.g. Flight/Hotel/Cab>",
        "details": "<Details about the booking>",
        "status": "<Confirmed/Pending/etc.>",
        "bookingId": "<Booking reference code>"
      }
      // More bookings as needed
    ],
    "Suggestions": [
      {
        "type": "heading",
        "content": "Personalized Suggestions for You"
      },
      {
        "type": "suggestion",
        "title": "<Suggestion Title>",
        "description": "<Concise suggestion or tip>",
        "category": "<Category e.g. Day Trip>"
      }
      // More suggestions as needed
    ],
    "Locations": [
      {
        "type": "heading",
        "content": "Key Locations in <city>"
      },
      {
        "type": "location",
        "name": "<Location Name>",
        "description": "<Location description>",
        "coordinates": "<Location coordinates>"
      }
      // More key locations
    ]
  }
}
Strict rules:

Output ONLY the JSON object in this format—do not explain, introduce, or comment on the output.

Each section and tab must follow the sample structure, including headings, types, and nesting. Field names, types, and order must not change.

Use clear, relevant, concise language throughout, filling each field meaningfully.

Add or omit array entries (activities, foods, bookings, etc.) as needed, but do not alter the structure or keys.

If content is missing, leave fields as empty strings or empty arrays (never omit required keys).

No extra formatting, markdown, or non-JSON text should be produced.

Your job is done only when your output exactly matches this schema and all user-requested information is integrated into the relevant fields and sections.
"""



