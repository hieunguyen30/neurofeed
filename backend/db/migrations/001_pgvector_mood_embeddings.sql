-- Step 1: Enable pgvector extension (run once per database)
create extension if not exists vector;

-- Step 2: Create mood_embeddings table
create table if not exists mood_embeddings (
  id              uuid        primary key default gen_random_uuid(),
  session_id      text,
  raw_input       text        not null,
  embedding       vector(384) not null,
  keywords        text[],
  podcasts_returned jsonb,
  created_at      timestamptz default now()
);

-- Step 3: Lock down direct client access — backend uses service_role key which bypasses RLS.
-- No policies are added intentionally: only the service_role key (used by FastAPI) can read/write.
alter table mood_embeddings enable row level security;

-- Step 4: IVFFlat index for fast cosine similarity search
-- Note: IVFFlat needs ~1000+ rows to outperform a sequential scan.
-- On a fresh table this is a no-op cost-wise; add it now so it's ready.
create index if not exists mood_embeddings_embedding_idx
  on mood_embeddings
  using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

-- Step 5: RPC function called by the Python client for similarity search
create or replace function match_mood_embeddings(
  query_embedding   vector(384),
  similarity_threshold float,
  match_count       int
)
returns table (
  id                uuid,
  session_id        text,
  raw_input         text,
  keywords          text[],
  podcasts_returned jsonb,
  similarity        float
)
language plpgsql
as $$
begin
  return query
  select
    me.id,
    me.session_id,
    me.raw_input,
    me.keywords,
    me.podcasts_returned,
    1 - (me.embedding <=> query_embedding) as similarity
  from mood_embeddings me
  where 1 - (me.embedding <=> query_embedding) > similarity_threshold
  order by me.embedding <=> query_embedding
  limit match_count;
end;
$$;
