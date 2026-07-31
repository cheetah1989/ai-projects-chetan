from http.client import responses
from dotenv import load_dotenv
from google import genai
from config import get_api_key
import json
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
    You are an expert meeting assistant.
    Analyze the following meeting transcript and return ONLY valid JSON.
    Do not include markdown.
    Do not include explanations.
    Do not wrap the JSON in triple backticks.

    Transcript:
    {transcript}

    Return the JSON in exactly this structure:
    {{
        "meeting_title": "",
        "meeting_summary": "",
        "participants": [],
        "action_items": [
            {{
                "owner": "",
                "task": "",
                "due_date": "",
                "status": ""
            }}
        ],
        "decisions": [],
        "pending_items": []
    }}
    Rules:
    - meeting_summary should be 3-5 sentences.
    - participants should contain only participant names.
    - action_items should be a list of objects.
    - decisions should contain only agreed decisions.
    - pending_items should contain unresolved items.
    - If a section has no data, return an empty list.
    - If information is unavailable, use an empty string or empty list.
    - Return valid JSON only.
    """
    response = client.models.generate_content(
        model= get_model_name(),
        contents=prompt
    )

    try:
        summary= json.loads(response.text)
        return summary
    except json.JSONDecodeError as e:
        raise ValueError (
            f"LLM Didn't generate valid JSON output: {e}"
        )

