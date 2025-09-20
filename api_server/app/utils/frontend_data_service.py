from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

# Dummy data from ui-server/src/constants/planData.js
plan_data = {
  "city": "Pune, India",
  "dates": "Oct 25 → Oct 30",
  "locations": "Sinhgad fort, Khadakwasla, Shanirwada & 13 more",
  "notes": "Any Notes to save?",
  "tripDescription": {
    "title": "Your trip to Pune ....................",
    "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
  },
  "tabs": ["Overview", "Itinerary", "Food", "Bookings", "Suggestions", "Locations", "Weather", "Packing", "Documents", "Budget"],
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
      },
      {
        "type": "departure",
        "days": 10,
        "time": "14:30:55"
      }
    ],
    "Itinerary": [
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
                "time": None,
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
            ],
            "dailyCost": {
              "amount": 5000,
              "currency": "₹",
              "details": "Activities: ₹2000, Food: ₹1500, Travel: ₹1500"
            }
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
            ],
            "dailyCost": {
              "amount": 4500,
              "currency": "₹",
              "details": "Activities: ₹1800, Food: ₹1200, Shopping: ₹1500"
            }
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
            ],
            "dailyCost": {
              "amount": 6000,
              "currency": "₹",
              "details": "Activities: ₹2500, Food: ₹1500, Wine Tasting: ₹2000"
            }
          }
        ]
      },
      {
        "type": "packageTourMention",
        "content": "Existing packages have been combined for a day tour, saving ₹1000."
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
      },
      {
        "type": "packageBooking",
        "service": "Day Tour Package",
        "details": "Sinhgad Fort & Khadakwasla Dam Combined Tour",
        "status": "Confirmed",
        "bookingId": "PKG123456",
        "savings": {
          "amount": 1000,
          "currency": "₹"
        },
        "message": "You saved ₹1000 by booking this combined package!"
      },
      {
        "type": "bookingConfirmation",
        "confirmedMessage": "Booking Confirmed! Your adventure begins on Nov 20, 2024.",
        "referenceNo": "ABC1245",
        "emailMessage": "All details emailed to you"
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
    ],
    "Weather": [
      {
        "type": "heading",
        "content": "Weather Forecast"
      },
      {
        "type": "weather",
        "city": "Kyoto",
        "icon": "☀️",
        "temperature": "20-24°C"
      },
      {
        "type": "weather",
        "city": "Osaka",
        "icon": "☁️",
        "temperature": "20-24°C"
      },
      {
        "type": "weather",
        "city": "Nara",
        "icon": "🌧️",
        "temperature": "18-22°C"
      }
    ],
    "Packing": [
      {
        "type": "heading",
        "content": "Packing Checklist"
      },
      { "type": "item", "name": "Passport", "checked": True },
      { "type": "item", "name": "Visa", "checked": False },
      { "type": "item", "name": "Rain Jacket", "checked": False },
      { "type": "item", "name": "Comfortable Shoes", "checked": True },
      { "type": "item", "name": "Universal Adapter", "checked": False },
      { "type": "item", "name": "Camera", "checked": True },
      { "type": "item", "name": "Portable Charger", "checked": False }
    ],
    "Documents": [
      {
        "type": "heading",
        "content": "Important Documents"
      },
      { "type": "document", "name": "E Tickets (PDF)", "icon": "📄" },
      { "type": "document", "name": "Travel Insurance (P955)", "icon": "📄" },
      { "type": "document", "name": "Hotel Booking Confirmation (PDF)", "icon": "🏨" },
      { "type": "document", "name": "Car Rental Voucher (PDF)", "icon": "🚗" }
    ],
    "Budget": [
      {
        "type": "heading",
        "content": "Budget Tracker"
      },
      {
        "type": "budget",
        "spent": 40000,
        "total": 50000,
        "currency": "₹"
      }
    ]
  }
}

# Dummy data from ui-server/src/constants/promptCards.js
prompt_cards_data = [
  {
    "id": 1,
    "displayText": 'Romantic Paris Getaway',
    "promptText": 'Plan a romantic getaway to Paris for two, including flights, accommodation, and suggestions for romantic activities and dining.',
  },
  {
    "id": 2,
    "displayText": 'Amazon Rainforest Adventure',
    "promptText": 'Organize an adventure trip to the Amazon rainforest, focusing on eco-tourism, wildlife viewing, and local cultural experiences.',
  },
  {
    "id": 3,
    "displayText": 'Disney World Family Vacation',
    "promptText": 'Plan a family vacation to Disney World for a family of four, including park tickets, accommodation, and kid-friendly activities.',
  },
  {
    "id": 4,
    "displayText": 'Solo Backpacking Southeast Asia',
    "promptText": 'Create a solo backpacking itinerary through Southeast Asia for one month, covering budget-friendly options and must-see destinations.',
  },
]

# Dummy data from ui-server/src/constants/tripData.js
trip_data = {
    "booking": {
        "confirmedMessage": "Booking Confirmed! Your adventure begins on Nov 20, 2024.",
        "referenceNo": "ABC1245",
        "emailMessage": "All details emailed to you"
    },
    "departure": {
        "days": 10,
        "time": "14:30:55"
    },
    "weatherForecast": [
        {
            "city": "Kyoto",
            "icon": "☀️",
            "temperature": "20-24°C"
        },
        {
            "city": "Osaka",
            "icon": "☁️",
            "temperature": "20-24°C"
        },
        {
            "city": "Nara",
            "icon": "🌧️",
            "temperature": "18-22°C"
        }
    ],
    "itinerary": [
        {
            "day": 1,
            "title": "Arrive in Kyoto",
            "activities": [
                "Check into Kyolo Garden Inn (15:00)",
                "Dinner at local ramen shop (19:00)",
                "Evening stroll around Gion district (21:00)"
            ]
        },
        {
            "day": 2,
            "title": "Explore Temples",
            "activities": [
                "Fushimi Inari Shrine (9:00)",
                "Kiyomizu-dera (13:00)",
                "Sanjusangendo Temple (16:00)"
            ]
        },
        {
            "day": 3,
            "title": "Nara Day Trip",
            "activities": [
                "Travel to Nara (8:00)",
                "Visit Todai-ji Temple and Nara Park (10:00)",
                "Feed deer (12:00)",
                "Return to Kyoto (17:00)"
            ]
        }
    ],
    "packingChecklist": [
        { "item": "Passport", "checked": True },
        { "item": "Visa", "checked": False },
        { "item": "Rain Jacket", "checked": False },
        { "item": "Comfortable Shoes", "checked": True },
        { "item": "Universal Adapter", "checked": False },
        { "item": "Universal Adaptis", "checked": False },
        { "item": "Camera", "checked": True },
        { "item": "Portable Charger", "checked": False }
    ],
    "timelulies": [
        "Kortel Vouchers Shoes",
        "Uzenji-tei (11:00)",
        "Tea Ceremony Reservation (14:00)",
        "Ryokan Check-in (16:00)"
    ],
    "notifications": [
        "✈️ Flight JL456 delayed by minutes.",
        "Nov 22, expect crowds.",
        "Reminder: Check-in for your flight 24 hours prior to departure.",
        "New exclusive offer: 10% off on local tours!"
    ],
    "documents": [
        "📄 E Tickets (PDF)",
        "📄 Travel Insurance (P955)",
        "🏨 Hotel Booking Confirmation (PDF)",
        "🚗 Car Rental Voucher (PDF)"
    ],
    "budgetTracker": {
        "spent": 40000,
        "total": 50000,
        "currency": "₹"
    }
}

# Dummy data from ui-server/src/constants/unifiedTripData.js
unified_trip_data = {
  "city": "Pune, India",
  "dates": "Oct 25 → Oct 30",
  "locations": "Sinhgad fort, Khadakwasla, Shanirwada & 13 more",
  "notes": "Any Notes to save?",
  "tripDescription": {
    "title": "Your trip to Pune ....................",
    "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
  },
  "tabs": ["Overview", "Itinerary", "Food", "Bookings", "Suggestions", "Locations", "Weather", "Packing", "Documents", "Budget"],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "This is the overview content for your trip. It includes general information and highlights about the city, its culture, and what to expect during your visit."
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
      },
      {
        "type": "departure",
        "days": 10,
        "time": "14:30:55"
      }
    ],
    "Itinerary": [
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
                "time": None,
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
      },
      {
        "type": "bookingConfirmation",
        "confirmedMessage": "Booking Confirmed! Your adventure begins on Nov 20, 2024.",
        "referenceNo": "ABC1245",
        "emailMessage": "All details emailed to you"
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
    ],
    "Weather": [
      {
        "type": "heading",
        "content": "Weather Forecast"
      },
      {
        "type": "weather",
        "city": "Kyoto",
        "icon": "☀️",
        "temperature": "20-24°C"
      },
      {
        "type": "weather",
        "city": "Osaka",
        "icon": "☁️",
        "temperature": "20-24°C"
      },
      {
        "type": "weather",
        "city": "Nara",
        "icon": "🌧️",
        "temperature": "18-22°C"
      }
    ],
    "Packing": [
      {
        "type": "heading",
        "content": "Packing Checklist"
      },
      { "type": "item", "name": "Passport", "checked": True },
      { "type": "item", "name": "Visa", "checked": False },
      { "type": "item", "name": "Rain Jacket", "checked": False },
      { "type": "item", "name": "Comfortable Shoes", "checked": True },
      { "type": "item", "name": "Universal Adapter", "checked": False },
      { "type": "item", "name": "Camera", "checked": True },
      { "type": "item", "name": "Portable Charger", "checked": False }
    ],
    "Documents": [
      {
        "type": "heading",
        "content": "Important Documents"
      },
      { "type": "document", "name": "E Tickets (PDF)", "icon": "📄" },
      { "type": "document", "name": "Travel Insurance (P955)", "icon": "📄" },
      { "type": "document", "name": "Hotel Booking Confirmation (PDF)", "icon": "🏨" },
      { "type": "document", "name": "Car Rental Voucher (PDF)", "icon": "🚗" }
    ],
    "Budget": [
      {
        "type": "heading",
        "content": "Budget Tracker"
      },
      {
        "type": "budget",
        "spent": 40000,
        "total": 50000,
        "currency": "₹"
      }
    ]
  }
}


def get_plan_data() -> Dict[str, Any]:
    return plan_data

def get_prompt_cards_data() -> List[Dict[str, Any]]:
    return prompt_cards_data

def get_trip_data() -> Dict[str, Any]:
    return trip_data

def get_unified_trip_data() -> Dict[str, Any]:
    return unified_trip_data

trip_cards_data = [
  {
    "id": 1,
    "title": "My Europe Grand Tour",
    "description": "14 days, 7 cities, culture & cuisine across Europe.",
    "imageUrl": "/map_bg.png"
  },
  {
    "id": 2,
    "title": "Coastal California Road Trip",
    "description": "7 days of scenic drives and charming beach towns.",
    "imageUrl": "/map_bg.png"
  },
  {
    "id": 3,
    "title": "Japanese Cherry Blossom Adventure",
    "description": "10 days of ancient temples & modern Tokyo during cherry blossom season.",
    "imageUrl": "/map_bg.png"
  }
]

def get_trip_cards_data() -> List[Dict[str, Any]]:
    return trip_cards_data
