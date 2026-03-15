import os
from supabase import create_client, Client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

async def save_mood_history(user_input: str, mood: str, keywords: list, reason: str):
    data = {
        "user_input": user_input,
        "mood": mood,
        "keywords": keywords,
        "reason": reason
    }
    
    supabase.table("mood_history").insert(data).execute()