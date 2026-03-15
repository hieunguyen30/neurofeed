from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.mood_service import detect_mood
from services.podcast_service import get_podcasts

router = APIRouter()

class RecommendRequest(BaseModel):
    user_input: str

@router.post("/recommend")
async def recommend(request: RecommendRequest):
    try:
        # Step 1: Detect mood using Claude
        mood_result = await detect_mood(request.user_input)
        
        # Step 2: Fetch podcasts based on mood
        podcasts = await get_podcasts(mood_result["keywords"])
        
        return {
            "mood": mood_result["mood"],
            "reason": mood_result["reason"],
            "podcasts": podcasts
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))