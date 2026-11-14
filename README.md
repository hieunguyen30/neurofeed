# Neurofeed 🎙️

**Podcast recommendations that fit your mood and your day.**

Tell Neurofeed how you're feeling in plain language. It uses AI to understand your emotional state, checks what your day looks like on your calendar, and suggests podcasts that match your headspace. The more you use it, the better it gets: past moods and the podcasts that fit them are remembered and blended into future recommendations.

---

## How it works

```
"feeling drained after a long day"
        │
        ▼
 Claude API ──► mood + search keywords
        │
        ├──► Google Calendar ──► time of day, busy stretches, upcoming events (e.g. gym)
        │
        ▼
 all-MiniLM-L6-v2 ──► 384-dim mood embedding
        │
        ├──► pgvector: find similar past moods (cosine similarity ≥ 0.65)
        └──► Podcast Index API: fresh results from the keywords
        │
        ▼
 Blend fresh + historically matched podcasts (up to 8) ──► save to Supabase
```

1. **Describe your mood:** the user writes how they're feeling in natural language.
2. **Understand it:** Claude analyzes the text and returns a mood label plus search keywords.
3. **Add context:** Google Calendar data shapes recommendations around the time of day and what's coming up, like a packed afternoon or a gym session.
4. **Embed it:** the mood description is embedded with `all-MiniLM-L6-v2` into a 384-dimensional vector.
5. **Remember:** pgvector searches past embeddings for semantically similar moods (cosine similarity ≥ 0.65).
6. **Find podcasts:** the keywords query the Podcast Index API for fresh results.
7. **Blend:** if similar past moods exist, the podcasts that matched them are mixed in with the fresh results (up to 8 total).
8. **Learn:** the new embedding and its results are saved to Supabase for future requests.

---

## Tech stack

| Layer | Tools |
|---|---|
| **Frontend** | Next.js 15, TypeScript, Tailwind CSS |
| **Backend** | FastAPI (Python), Dockerized and deployed on Render |
| **AI** | Anthropic Claude API (`claude-opus-4-7`) for mood detection · `sentence-transformers` (`all-MiniLM-L6-v2`) for mood embeddings |
| **Database** | Supabase (PostgreSQL) for mood history and embeddings · `pgvector` for cosine similarity search |
| **Integrations** | Google Calendar API for schedule context · Podcast Index API for podcast search |
| **CI/CD** | GitHub Actions |

---

## Configuration

The app needs credentials for:
- **Anthropic:** Claude API key
- **Supabase:** project URL and key, with the `pgvector` extension enabled
- **Podcast Index:** API key and secret
- **Google Calendar:** OAuth client credentials

Set these as environment variables for the backend (and the frontend where needed) before running.

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
