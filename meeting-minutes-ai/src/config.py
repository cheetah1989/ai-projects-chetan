from dotenv import load_dotenv
import os
#Load variables from the .env files into the environment

load_dotenv()

def get_api_key() -> str:
    """
    Returns Gemini API Key from the environment file
    Raises an error if missing
    """
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "LLM API key not found. Make sure .env file is having the key "
        )

    return api_key