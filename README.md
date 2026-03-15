# Neurofeed 🎙️

A mood-aware podcast recommendation app. Tell it how you're feeling — it detects your emotional state using AI and suggests podcasts matched to your headspace.

## Tech Stack

**Frontend**
- Next.js 15, TypeScript, Tailwind CSS

**Backend**
- FastAPI, Python
- Dockerized + deployed on Render

**AI**
- Groq API (llama-3.3-70b) for mood detection

**Database**
- Supabase (PostgreSQL) — stores mood history per session

**Podcasts**
- Podcast Index API

## How It Works

1. User describes how they're feeling in natural language
2. Groq LLM analyzes the text and returns a mood + search keywords
3. Keywords are used to query the Podcast Index API
4. Results are ranked and returned to the frontend
5. Session is saved to Supabase for future personalization

## Running Locally

**Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

**Environment Variables**

Create a `.env` file in `/backend`:
```
GROQ_API_KEY=
SUPABASE_URL=
SUPABASE_KEY=
PODCAST_INDEX_KEY=
PODCAST_INDEX_SECRET=
```

## Docker
```bash
cd backend
docker build -t neurofeed-backend .
docker run -p 8000:8000 --env-file .env neurofeed-backend
```

## Deployment
- Backend: Render (Docker)
- Frontend: coming soon
- CI/CD: GitHub Actions — auto-deploys to Render on push to `main`