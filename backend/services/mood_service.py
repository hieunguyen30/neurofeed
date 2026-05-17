import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a mood analyzer. Given a user's text, return ONLY a JSON object with:
- mood: one of (happy, sad, stressed, focused, energetic, tired, anxious)
- keywords: a list of 2-3 short podcast search terms (1-2 words max each, e.g. "meditation", "focus", "sleep", "stoicism", "anxiety" — NOT phrases like "stress management techniques")
- reason: one sentence explaining the mood detection

Example response:
{
    "mood": "stressed",
    "keywords": ["meditation", "calm", "anxiety"],
    "reason": "User seems overwhelmed and needs calming content"
}

Return only valid JSON, no extra text."""


async def detect_mood(user_input: str) -> dict:
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=500,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
    )

    response_text = message.content[0].text
    mood_data = json.loads(response_text)
    return mood_data
