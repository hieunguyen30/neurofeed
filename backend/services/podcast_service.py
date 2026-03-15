import os
import httpx

# async def get_podcasts(keywords: list) -> list:
#     search_query = " ".join(keywords)
    
#     api_key = os.getenv("PODCAST_INDEX_KEY")
#     api_secret = os.getenv("PODCAST_INDEX_SECRET")
    
#     import time
#     import hashlib
    
#     epoch_time = int(time.time())
#     data_to_hash = api_key + api_secret + str(epoch_time)
#     sha_1 = hashlib.sha1(data_to_hash.encode()).hexdigest()
    
#     headers = {
#         "X-Auth-Date": str(epoch_time),
#         "X-Auth-Key": api_key,
#         "Authorization": sha_1,
#         "User-Agent": "Neurofeed/1.0"
#     }
    
#     async with httpx.AsyncClient() as client:
#         response = await client.get(
#             "https://api.podcastindex.org/api/1.0/search/byterm",
#             headers=headers,
#             params={"q": search_query, "max": 3}
#         )
        
#         data = response.json()
#         podcasts = []
        
#         for feed in data.get("feeds", []):
#             podcasts.append({
#                 "title": feed.get("title"),
#                 "description": feed.get("description"),
#                 "image": feed.get("image"),
#                 "url": feed.get("link")
#             })
        
#         return podcasts

async def get_podcasts(keywords: list) -> list:
    return [
        {
            "title": "Calm Minds",
            "description": "A relaxing podcast for stress relief",
            "image": "",
            "url": "https://example.com"
        },
        {
            "title": "Meditation Daily",
            "description": "Daily guided meditation sessions",
            "image": "",
            "url": "https://example.com"
        },
        {
            "title": "Deep Breath",
            "description": "Breathing exercises for anxiety",
            "image": "",
            "url": "https://example.com"
        }
    ]