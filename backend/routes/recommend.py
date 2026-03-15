from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.mood_service import detect_mood
from services.podcast_service import get_podcasts
from db.supabase import save_mood_history

router = APIRouter()

class RecommendRequest(BaseModel):
    user_input: str

@router.post("/recommend")
async def recommend(request: RecommendRequest):
    try:
        mood_result = await detect_mood(request.user_input)
        print("MOOD RESULT:", mood_result)  # ADD THIS
        
        podcasts = await get_podcasts(mood_result["keywords"])
        print("PODCASTS:", podcasts)  # ADD THIS
        
        await save_mood_history(
            user_input=request.user_input,
            mood=mood_result["mood"],
            keywords=mood_result["keywords"],
            reason=mood_result["reason"]
        )
        print("SAVED TO DB")  # ADD THIS
        
        return {
            "mood": mood_result["mood"],
            "reason": mood_result["reason"],
            "podcasts": podcasts
        }
    except Exception as e:
        print("ERROR:", str(e))  # ADD THIS
        raise HTTPException(status_code=500, detail=str(e))