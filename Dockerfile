FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (cache layer)
COPY rag/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (from rag/ subdir)
COPY rag/ /app/

# Copy corpus (from corpus/ subdir at root)
COPY corpus/ /app/corpus/

# Run indexer at build time (BM25-only, fast, ~30s)
RUN SKIP_EMBEDDINGS=1 CORPUS_PATH=/app/corpus python index.py

EXPOSE 8000

# PORT is injected by Railway at runtime
CMD uvicorn api:app --host 0.0.0.0 --port ${PORT:-8000}
