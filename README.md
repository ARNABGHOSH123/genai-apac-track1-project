# Aesthetic Weather Assistant 🌤️👗

A conversational AI agent built with Google's Agent Development Kit (ADK) that transcends traditional weather data reporting. This assistant acts as a personalized lifestyle companion, translating raw meteorological data into actionable fashion advice, vibe-matching activities, and curated recommendations.

## 📊 Process Flow Diagram

![Process Flow Diagram](assets/process_flow.svg)

## 🌟 Features

- **Live Weather Integration:** Fetches real-time, accurate meteorological data for any specified location using WeatherAPI.
- **Conversational Onboarding:** Acknowledges user greetings and proactively introduces its capabilities to set clear expectations.
- **Contextual Fashion Advice:** Synthesizes weather conditions into practical, stylish, and comfortable outfit recommendations.
- **Vibe-Matching Recommendations:** Suggests complementary activities, beverages, and music genres suited to the current atmospheric "vibe".
- **Strict Topic Guardrails:** Built-in conversational constraints ensure the agent remains laser-focused on weather, clothing, and activities, politely deflecting unrelated prompts.

## 🏗️ Technologies Used

- **Google Agent Development Kit (ADK):** Core framework for defining the agent, handling tool execution, and constructing the persona.
- **Google Gemini LLM (`gemini-3-flash-preview`):** The underlying foundation model for natural language understanding and text synthesis.
- **WeatherAPI & `requests`:** For executing secure HTTP requests to fetch live JSON weather data.
- **Python `dotenv`:** To safely manage API keys and environment variables.
- **`certifi` & `os`:** Dynamically resolves SSL certificate paths for robust local execution.

## 🚀 Setup & Installation

1. **Set up your environment:**
   Ensure you have your Python virtual environment activated.

   ```bash
   .\venv\Scripts\Activate.ps1
   ```

2. **Install the dependencies:**
   Make sure you have installed the necessary requirements.

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Make sure your `.env` file in the root directory contains your [WeatherAPI Key](https://www.weatherapi.com/):
   ```ini
   WEATHERAPI_KEY=your_api_key_here
   GEMINI_MODEL=gemini-3-flash-preview
   ```

## 💡 Usage

Run your agent using the ADK interface. You can interact with the agent by asking things like:

- _"Hi!"_
- _"What's the weather like in Tokyo right now?"_
- _"It's gloomy in London, what should I wear and do to match the vibe?"_

The agent will seamlessly handle the live API calls, execute the guardrails, and provide a deeply curated, stylish response!
