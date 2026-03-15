import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def detect_mood(user_input: str) -> dict:
    message = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=500,
        messages=[
            {
                "role": "system",
                "content": """You are a mood analyzer. Given a user's text, return ONLY a JSON object with:
                - mood: one of (happy, sad, stressed, focused, energetic, tired, anxious)
                - keywords: a list of 2-3 podcast search keywords matching their mood
                - reason: one sentence explaining the mood detection
                
                Example response:
                {
                    "mood": "stressed",
                    "keywords": ["meditation", "calm", "stress relief"],
                    "reason": "User seems overwhelmed and needs calming content"
                }
                
                Return only valid JSON, no extra text."""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    
    response_text = message.choices[0].message.content
    print("GROQ RESPONSE:", response_text)  # ADD THIS
    mood_data = json.loads(response_text)
    return mood_data