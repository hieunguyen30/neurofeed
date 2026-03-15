from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.recommend import router as recommend_router

load_dotenv()

app = FastAPI(title="Neurofeed API")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(recommend_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}