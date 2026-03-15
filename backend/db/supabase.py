import os
from supabase import create_client, Client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

async def save_mood_history(user_input: str, mood: str, keywords: list, reason: str) -> str:  # str not int
    data = {
        "user_input": user_input,
        "mood": mood,
        "keywords": keywords,
        "reason": reason
    }
    
    result = supabase.table("mood_history").insert(data).execute()
    return result.data[0]["id"]  # returns uuid string


async def save_clicked_podcast(history_id: str, podcast_title: str):  # str not int
    supabase.table("mood_history").update(
        {"clicked_podcast": podcast_title}
    ).eq("id", history_id).execute()