import os
from dotenv import load_dotenv
from google.cloud import secretmanager

if os.path.exists(".env.development") and not os.getenv("PRODUCTION"):
    load_dotenv(dotenv_path=os.path.join(
        os.getcwd(), '.env.development'), override=True)
elif os.getenv("GOOGLE_CLOUD_PROJECT"):
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    settings_name = os.getenv(
        "SETTINGS_NAME", "GENAI_TRACK1_PROJECT_SECRET")
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(
        name=name).payload.data.decode("UTF-8")
    for line in payload.split("\n"):
        key, value = line.split("=", 1)
        os.environ[key] = value
else:
    raise RuntimeError("No .env.development file found and not running in GCP")


class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")
    AGENT_MODEL = os.getenv("AGENT_MODEL")
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
    GOOGLE_GENAI_USE_VERTEXAI= os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "false").lower() == "true"
    GOOGLE_CLOUD_LOCATION=os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")