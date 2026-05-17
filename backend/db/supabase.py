import os
from supabase import create_client, Client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)


async def save_mood_history(user_input: str, mood: str, keywords: list, reason: str) -> str:
    data = {
        "user_input": user_input,
        "mood": mood,
        "keywords": keywords,
        "reason": reason,
    }
    result = supabase.table("mood_history").insert(data).execute()
    return result.data[0]["id"]


async def save_clicked_podcast(history_id: str, podcast_title: str):
    supabase.table("mood_history").update(
        {"clicked_podcast": podcast_title}
    ).eq("id", history_id).execute()


async def save_mood_embedding(
    raw_input: str,
    embedding: list[float],
    keywords: list[str],
    podcasts_returned: list[dict],
    session_id: str | None = None,
) -> str:
    data: dict = {
        "raw_input": raw_input,
        "embedding": embedding,
        "keywords": keywords,
        "podcasts_returned": podcasts_returned,
    }
    if session_id:
        data["session_id"] = session_id
    result = supabase.table("mood_embeddings").insert(data).execute()
    return result.data[0]["id"]


async def find_similar_moods(
    embedding: list[float],
    threshold: float = 0.65,
    limit: int = 5,
) -> list[dict]:
    result = supabase.rpc(
        "match_mood_embeddings",
        {
            "query_embedding": embedding,
            "similarity_threshold": threshold,
            "match_count": limit,
        },
    ).execute()
    return result.data or []