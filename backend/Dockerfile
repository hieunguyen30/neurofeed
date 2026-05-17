FROM python:3.13-slim

WORKDIR /app

# Install CPU-only PyTorch first to prevent pip from pulling the ~2 GB CUDA build
# when sentence-transformers resolves its torch dependency.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download and cache the model at build time so containers start instantly.
# This layer is invalidated only when the model name changes.
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
