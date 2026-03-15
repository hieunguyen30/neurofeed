import os
import json
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

async def detect_mood(user_input: str) -> dict:
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=500,
        system="""You are a mood analyzer. Given a user's text, return ONLY a JSON object with:
        - mood: one of (happy, sad, stressed, focused, energetic, tired, anxious)
        - keywords: a list of 2-3 podcast search keywords matching their mood
        - reason: one sentence explaining the mood detection
        
        Example response:
        {
            "mood": "stressed",
            "keywords": ["meditation", "calm", "stress relief"],
            "reason": "User seems overwhelmed and needs calming content"
        }
        
        Return only valid JSON, no extra text.""",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    response_text = message.content[0].text
    mood_data = json.loads(response_text)
    return mood_dataisan a