from http.client import responses
from dotenv import load_dotenv
from google import genai
from config import get_api_key
import os

client = genai.Client(api_key=get_api_key())
llm_model = load_dotenv("GEMINI_MODEL")

def get_model_name() -> str:
    model = os.getenv("GEMINI_MODEL")

    if not model:
        print("No LLM Model found, update the .env file with model name")
        exit(1)
    return model

def summarize_transcript(transcript: str) -> dict:
    """
    Sends transcript to LLM and gets the summary 
    """
    prompt = f"""
     You are expert meeting assistant.
     Summarize the following meeting transcript in a professional way. 
     Transcript:
     {transcript}
    """
    response = client.models.generate_content(
        model= get_model_name(),
        contents=prompt
    )

    return response.text