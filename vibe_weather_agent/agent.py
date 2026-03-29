import os
import requests
import certifi
from google.adk.agents.llm_agent import LlmAgent
from config import Config
from base_model import base_model

# Fix for invalid global SSL_CERT_FILE environment variable
if 'SSL_CERT_FILE' in os.environ and not os.path.exists(os.environ['SSL_CERT_FILE']):
    os.environ['SSL_CERT_FILE'] = certifi.where()

WEATHERAPI_KEY = Config.WEATHERAPI_KEY


# Real tool implementation fetching live weather
def get_current_weather(location: str) -> dict:
    """Returns the current weather in a specified location using the WeatherAPI."""
    if not WEATHERAPI_KEY or WEATHERAPI_KEY == "your_api_key_here":
        return {"status": "error", "message": "WEATHERAPI_KEY is missing or invalid in .env"}
    
    url = f"https://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={location}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

root_agent = LlmAgent(
    model=base_model,
    name='vibe_weather_agent',
    description="Fetches the current weather in a specified location.",
    instruction=(
        "You are a helpful, conversational, and stylish weather assistant. "
        "When the user greets you (e.g., 'hi', 'hello'), you must introduce yourself and clearly explain what you can do (i.e., checking the weather, suggesting outfits, and recommending vibe-matching activities).\n\n"
        "Use the 'get_current_weather' tool to fetch weather details for the requested location.\n\n"
        "When providing the weather, instead of just reporting numbers, you must:\n"
        "1. Give a quick, engaging summary of the exact weather and temperature.\n"
        "2. Suggest a practical but stylish outfit suitable for this weather.\n"
        "3. Suggest an activity, a drink, or a type of music that perfectly matches the 'vibe' of the current conditions.\n\n"
        "STRICT RULE: You must ONLY answer questions related to weather, clothing, and weather-appropriate activities. "
        "If the user asks any off-topic questions, politely decline to answer and steer the conversation back to checking the weather."
    ),
    tools=[get_current_weather],
)

