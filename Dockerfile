FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app/

# Run indexer at build time (BM25-only, fast, ~30s)
RUN SKIP_EMBEDDINGS=1 CORPUS_PATH=/app/corpus python index.py

EXPOSE 8000

# PORT is injected by Railway at runtime
CMD bash -c 'uvicorn api:app --host 0.0.0.0 --port ${PORT:-8000}'
