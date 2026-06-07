"""
Growthwick Marketing Advisor API
FastAPI backend for the RAG-powered marketing advisor.

Run locally: uvicorn api:app --reload --port 8000
"""

import os
import numpy as np
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from models import QueryRequest, QueryResponse, ChunkSource, HealthResponse, PersonaInfo
from retrieve import get_retriever
from prompts import get_system_prompt, build_user_message

# OpenAI key (may be @vault ref in subprocess — check Azure fallback)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Azure OpenAI (HHX Foundation deployment — always available)
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")

# Anthropic key (check if real or @vault placeholder)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Pick LLM backend
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")  # Azure gpt-4o deployment

USE_AZURE_OPENAI = bool(AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT)
USE_ANTHROPIC = bool(ANTHROPIC_API_KEY and not ANTHROPIC_API_KEY.startswith("@vault"))
USE_OPENAI = bool(OPENAI_API_KEY and not OPENAI_API_KEY.startswith("@vault"))

CORPUS_PATH = os.getenv("CORPUS_PATH", str(Path(__file__).parent.parent / "corpus"))

app = FastAPI(
    title="Growthwick Marketing Advisor",
    description="RAG-powered marketing advisor grounded in 16 expert personas",
    version="1.0.0"
)

# CORS — allow all origins for now (tighten in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
frontend_path = Path(__file__).parent / "frontend"
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")


@app.on_event("startup")
async def startup_event():
    """Initialize retriever on startup."""
    retriever = get_retriever()
    stats = retriever.get_stats()
    print(f"Growthwick API started. Corpus: {stats['total_chunks']} chunks, {stats['personas']} personas")


@app.get("/")
async def root():
    """Serve the frontend."""
    index_path = frontend_path / "index.html"
    if index_path.exists():
        return FileResponse(str(index_path))
    return {"message": "Growthwick Marketing Advisor API", "docs": "/docs"}


@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check with corpus stats."""
    retriever = get_retriever()
    stats = retriever.get_stats()
    return HealthResponse(
        status="ok",
        total_chunks=stats["total_chunks"],
        personas=stats["personas"],
        corpus_path=CORPUS_PATH
    )


@app.get("/personas", response_model=List[PersonaInfo])
async def personas():
    """List all indexed personas with chunk counts."""
    retriever = get_retriever()
    return [PersonaInfo(**p) for p in retriever.get_personas()]


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """Main query endpoint. Runs hybrid retrieval + LLM generation."""
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    if not USE_AZURE_OPENAI and not USE_ANTHROPIC and not USE_OPENAI:
        raise HTTPException(status_code=500, detail="No LLM API configured.")

    retriever = get_retriever()

    # Generate query embedding via Azure OpenAI (supports text-embedding-3-small)
    query_embedding = None
    if USE_AZURE_OPENAI:
        try:
            from openai import AzureOpenAI
            az_client = AzureOpenAI(
                api_key=AZURE_OPENAI_KEY,
                azure_endpoint="https://hhx-ai-agents-general.openai.azure.com",
                api_version="2024-12-01-preview"
            )
            emb_response = az_client.embeddings.create(
                model="text-embedding-3-small",
                input=request.query
            )
            query_embedding = np.array(emb_response.data[0].embedding, dtype=np.float32)
        except Exception as e:
            print(f"Embedding failed (BM25-only fallback): {e}")
            query_embedding = None
    elif USE_OPENAI:
        try:
            from openai import OpenAI
            oa_client = OpenAI(api_key=OPENAI_API_KEY)
            emb_response = oa_client.embeddings.create(
                model="text-embedding-3-small",
                input=request.query
            )
            query_embedding = np.array(emb_response.data[0].embedding, dtype=np.float32)
        except Exception as e:
            print(f"Embedding failed (BM25-only fallback): {e}")
            query_embedding = None

    # Retrieve relevant chunks
    chunks = retriever.retrieve(
        query=request.query,
        query_embedding=query_embedding,
        persona_filter=request.persona_filter
    ) or []

    # Build prompt
    system_prompt = get_system_prompt()
    user_message = build_user_message(request.query, request.mode, chunks)

    # Call LLM — Azure OpenAI preferred (always available), then Anthropic, then OpenAI
    response_text = ""
    try:
        if USE_AZURE_OPENAI:
            from openai import AzureOpenAI
            az_client = AzureOpenAI(
                api_key=AZURE_OPENAI_KEY,
                azure_endpoint="https://hhx-ai-agents-general.openai.azure.com",
                api_version="2024-12-01-preview"
            )
            completion = az_client.chat.completions.create(
                model=LLM_MODEL,  # deployment name = model id on HHX Foundry
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            response_text = completion.choices[0].message.content
        elif USE_ANTHROPIC:
            import anthropic
            ant_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
            msg = ant_client.messages.create(
                model="claude-sonnet-4-5-20251001",
                max_tokens=2000,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}]
            )
            response_text = msg.content[0].text
        elif USE_OPENAI:
            from openai import OpenAI
            oa_client = OpenAI(api_key=OPENAI_API_KEY)
            completion = oa_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            response_text = completion.choices[0].message.content
    except Exception as e:
        import traceback
        print(f"LLM error: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"LLM call failed: {str(e)}")

    # Format sources
    sources = []
    for chunk in chunks:
        sources.append(ChunkSource(
            persona=chunk.get("persona", "unknown"),
            file_name=chunk.get("file_name", ""),
            source_url=chunk.get("source_url", ""),
            chunk_index=chunk.get("chunk_index", 0),
            type=chunk.get("type", "article"),
            text=chunk.get("chunk_text", "")[:500]  # truncate for response size
        ))

    return QueryResponse(
        response=response_text,
        sources=sources,
        mode=request.mode,
        query=request.query
    )
