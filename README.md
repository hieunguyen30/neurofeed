# Neurofeed 🎙️

A mood-aware podcast recommendation app. Tell it how you're feeling — it detects your emotional state using AI and suggests podcasts matched to your headspace.

## Tech Stack

**Frontend**
- Next.js 15, TypeScript, Tailwind CSS

**Backend**
- FastAPI, Python
- Dockerized + deployed on Render

**AI**
- Anthropic Claude API (claude-opus-4-7) for mood detection
- sentence-transformers (all-MiniLM-L6-v2) for mood embeddings

**Database**
- Supabase (PostgreSQL) — stores mood history and embeddings
- pgvector extension — cosine similarity search over past mood embeddings

**Podcasts**
- Podcast Index API

## How It Works

1. User describes how they're feeling in natural language
2. Claude (claude-opus-4-7) analyzes the text and returns a mood + search keywords
3. The mood description is embedded using all-MiniLM-L6-v2 (384-dim vector)
4. pgvector searches past embeddings for semantically similar moods (cosine similarity ≥ 0.65)
5. Keywords are used to query the Podcast Index API for fresh results
6. If similar past moods are found, their historically matched podcasts are blended in (up to 8 total)
7. The new embedding + results are saved to Supabase for future requests

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
ANTHROPIC_API_KEY=
SUPABASE_URL=
SUPABASE_KEY=        # must be the service_role key (not anon) — required for pgvector RLS
PODCAST_INDEX_KEY=
PODCAST_INDEX_SECRET=
```

**Database Setup**

Run the migration in the Supabase SQL editor before starting the backend:
```
backend/db/migrations/001_pgvector_mood_embeddings.sql
```
This enables pgvector, creates the `mood_embeddings` table with RLS, and registers the `match_mood_embeddings` RPC function.

## Docker
```bash
cd backend
docker build -t neurofeed-backend .   # downloads sentence-transformers model at build time
docker run -p 8000:8000 --env-file .env neurofeed-backend
```

## Deployment
- Backend: Render (Docker)
- Frontend: coming soon
- CI/CD: GitHub Actions — auto-deploys to Render on push to `main`