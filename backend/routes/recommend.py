import asyncio
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.mood_service import detect_mood
from services.podcast_service import get_podcasts
from services.embeddings import embed_text
from db.supabase import find_similar_moods, save_mood_embedding, save_mood_history

router = APIRouter()


class RecommendRequest(BaseModel):
    user_input: str


def _blend_podcasts(fresh: list[dict], historical: list[dict]) -> list[dict]:
    """Append historical podcasts that aren't already in the fresh list, up to 8 total."""
    seen = {p.get("url", "") for p in fresh}
    blended = list(fresh)
    for pod in historical:
        url = pod.get("url", "")
        if url and url not in seen:
            seen.add(url)
            blended.append(pod)
        if len(blended) >= 8:
            break
    return blended


@router.post("/recommend")
async def recommend(request: RecommendRequest):
    try:
        # Mood detection and embedding run first; podcast fetch + similarity search run in parallel after
        mood_result = await detect_mood(request.user_input)
        embedding = embed_text(request.user_input)

        podcasts, similar_moods = await asyncio.gather(
            get_podcasts(mood_result["keywords"]),
            find_similar_moods(embedding),
        )

        if similar_moods:
            historical: list[dict] = []
            for match in similar_moods:
                historical.extend(match.get("podcasts_returned") or [])
            podcasts = _blend_podcasts(podcasts, historical)

        # Persist both records concurrently after we have the final podcast list
        await asyncio.gather(
            save_mood_history(
                user_input=request.user_input,
                mood=mood_result["mood"],
                keywords=mood_result["keywords"],
                reason=mood_result["reason"],
            ),
            save_mood_embedding(
                raw_input=request.user_input,
                embedding=embedding,
                keywords=mood_result["keywords"],
                podcasts_returned=podcasts,
            ),
        )

        return {
            "mood": mood_result["mood"],
            "reason": mood_result["reason"],
            "podcasts": podcasts,
        }
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
