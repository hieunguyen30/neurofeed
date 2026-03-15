import os
import httpx
import time
import hashlib

async def get_podcasts(keywords: list) -> list:
    # Use only the first keyword for broader results
    search_query = keywords[0] if keywords else "mindfulness"
    
    api_key = os.getenv("PODCAST_INDEX_KEY")
    api_secret = os.getenv("PODCAST_INDEX_SECRET")
    
    epoch_time = int(time.time())
    data_to_hash = api_key + api_secret + str(epoch_time)
    sha_1 = hashlib.sha1(data_to_hash.encode()).hexdigest()
    
    headers = {
        "X-Auth-Date": str(epoch_time),
        "X-Auth-Key": api_key,
        "Authorization": sha_1,
        "User-Agent": "Neurofeed/1.0"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.podcastindex.org/api/1.0/search/byterm",
            headers=headers,
            params={"q": search_query, "max": 5}  # bumped to 5
        )
        data = response.json()
        podcasts = []
        
        for feed in data.get("feeds", []):
            podcasts.append({
                "title": feed.get("title"),
                "description": feed.get("description"),
                "image": feed.get("image"),
                "url": feed.get("link")
            })
        
        return podcasts