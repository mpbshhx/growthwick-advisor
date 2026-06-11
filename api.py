"""
Growthwick Marketing Advisor API
FastAPI backend for the RAG-powered marketing advisor.

Run locally: uvicorn api:app --reload --port 8000
"""

import os
import io
import re
import urllib.request
import urllib.error
import html
import numpy as np
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Request, Response, Depends, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from auth import authenticate, get_current_user, require_auth, logout

from models import QueryRequest, QueryResponse, ChunkSource, HealthResponse, PersonaInfo
from retrieve import get_retriever
from prompts import get_system_prompt, build_user_message
import chats_db

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
    """Initialize retriever + chat history DB on startup."""
    retriever = get_retriever()
    stats = retriever.get_stats()
    chats_db.init_db()
    print(f"Growthwick API started. Corpus: {stats['total_chunks']} chunks, {stats['personas']} personas. Chats DB: {chats_db.DB_PATH}")


@app.get("/login")
async def login_page():
    """Serve login page."""
    login_path = frontend_path / "login.html"
    return FileResponse(str(login_path))


@app.post("/auth/login")
async def auth_login(request: Request, response: Response):
    """Handle login form submission."""
    form = await request.form()
    username = str(form.get("username", ""))
    password = str(form.get("password", ""))
    token = authenticate(username, password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie("session", token, httponly=True, samesite="lax", max_age=259200)  # 3 days
    return response


@app.get("/auth/logout")
async def auth_logout(request: Request, response: Response):
    """Clear session and redirect to login."""
    logout(request, response)
    resp = RedirectResponse(url="/login", status_code=302)
    resp.delete_cookie("session")
    return resp


@app.get("/")
async def root(request: Request):
    """Serve the frontend — requires auth."""
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
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


def extract_text_from_file(filename: str, content: bytes) -> str:
    """Extract plain text from uploaded file. Supports PDF, DOCX, TXT, MD, images."""
    ext = Path(filename).suffix.lower()

    if ext == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(content))
            pages = [p.extract_text() or "" for p in reader.pages]
            text = "\n\n".join(pages).strip()
            return text[:50000]  # cap at 50k chars
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"PDF extraction failed: {e}")

    elif ext in (".docx",):
        try:
            from docx import Document
            doc = Document(io.BytesIO(content))
            text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
            return text[:50000]
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"DOCX extraction failed: {e}")

    elif ext in (".txt", ".md", ".csv", ".json"):
        try:
            return content.decode("utf-8", errors="replace")[:50000]
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"Text extraction failed: {e}")

    elif ext in (".png", ".jpg", ".jpeg", ".webp", ".gif"):
        # Use GPT-4o vision to describe the image
        return None  # handled separately in the endpoint

    else:
        raise HTTPException(status_code=422, detail=f"Unsupported file type: {ext}. Supported: PDF, DOCX, TXT, MD, PNG, JPG.")


def extract_urls(text: str) -> list:
    """Extract URLs from a string. Handles https://, http://, and bare www. domains."""
    urls = []
    # Full URLs with scheme
    full_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls.extend(re.findall(full_pattern, text))
    # Bare www. domains (no scheme) — prepend https://
    bare_pattern = r'(?<![/\w])www\.[a-zA-Z0-9][a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}(?:/[^\s<>"{}|\\^`\[\]]*)?'
    for match in re.findall(bare_pattern, text):
        candidate = 'https://' + match
        if candidate not in urls:
            urls.append(candidate)
    return urls[:3]


def fetch_url_content(url: str, timeout: int = 10) -> str:
    """Fetch a URL and return cleaned text content (strips HTML tags)."""
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; GrowthwickAdvisor/1.0)",
                "Accept": "text/html,application/xhtml+xml,*/*"
            }
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            encoding = resp.headers.get_content_charset() or "utf-8"
            body = raw.decode(encoding, errors="replace")

        # Strip script/style blocks
        body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r'<nav[^>]*>.*?</nav>', '', body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r'<header[^>]*>.*?</header>', '', body, flags=re.DOTALL | re.IGNORECASE)
        # Strip remaining HTML tags
        body = re.sub(r'<[^>]+>', ' ', body)
        # Decode HTML entities
        body = html.unescape(body)
        # Collapse whitespace
        body = re.sub(r'\s+', ' ', body).strip()
        return body[:40000]  # cap at 40k chars
    except urllib.error.HTTPError as e:
        return f"[Could not fetch URL: HTTP {e.code} {e.reason}]"
    except Exception as e:
        return f"[Could not fetch URL: {str(e)}]"


@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...), query: str = Form(default=""), mode: str = Form(default="strategy-build")):
    """Upload a file + optional question. Returns LLM analysis grounded in the file content."""
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not USE_AZURE_OPENAI:
        raise HTTPException(status_code=500, detail="No LLM configured.")

    content = await file.read()
    if len(content) > 20 * 1024 * 1024:  # 20MB limit
        raise HTTPException(status_code=413, detail="File too large. Max 20MB.")

    ext = Path(file.filename).suffix.lower()
    is_image = ext in (".png", ".jpg", ".jpeg", ".webp", ".gif")

    user_question = query.strip() or "Please review this document and provide strategic marketing feedback."

    from openai import AzureOpenAI
    az_client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        azure_endpoint="https://hhx-ai-agents-general.openai.azure.com",
        api_version="2024-12-01-preview"
    )

    system_prompt = get_system_prompt()

    if is_image:
        import base64
        b64 = base64.b64encode(content).decode()
        mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp", "gif": "image/gif"}.get(ext.lstrip("."), "image/png")
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": f"The user has uploaded an image named '{file.filename}'. {user_question}"},
                {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}}
            ]}
        ]
    else:
        file_text = extract_text_from_file(file.filename, content)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"""The user has uploaded a file named '{file.filename}'. Here is its content:

---BEGIN FILE CONTENT---
{file_text}
---END FILE CONTENT---

User's question: {user_question}

Please review this document through your marketing advisor lens. Provide specific, actionable feedback grounded in the expert frameworks you embody. Cite relevant frameworks where applicable."""}
        ]

    try:
        completion = az_client.chat.completions.create(
            model=LLM_MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=2000
        )
        response_text = completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM analysis failed: {str(e)}")

    # Persist to chat history (best-effort; failure does not break the response)
    conversation_id = None
    try:
        form = await request.form()
        conv_in = form.get("conversation_id")
        conversation_id = _persist_turn(
            username=user,
            conversation_id=str(conv_in) if conv_in else None,
            user_content=f"\U0001F4CE {file.filename}" + (f"\n\n{user_question}" if query.strip() else " \u2014 full review"),
            assistant_content=response_text or "",
            mode=mode,
            sources=None,
            file_meta={"filename": file.filename, "size": len(content), "ext": ext},
        )
    except Exception as e:
        print(f"chat persistence (upload) failed: {e}")

    return {
        "response": response_text,
        "filename": file.filename,
        "file_size": len(content),
        "mode": mode,
        "query": user_question,
        "conversation_id": conversation_id,
    }


@app.get("/personas", response_model=List[PersonaInfo])
async def personas():
    """List all indexed personas with chunk counts."""
    retriever = get_retriever()
    return [PersonaInfo(**p) for p in retriever.get_personas()]


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest, http_request: Request):
    """Main query endpoint — requires auth."""
    user = get_current_user(http_request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
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

    # Detect URLs in the query — fetch and inject page content
    urls = extract_urls(request.query)
    url_context = ""
    if urls:
        fetched_pages = []
        for url in urls[:3]:  # max 3 URLs
            page_text = fetch_url_content(url)
            fetched_pages.append(f"URL: {url}\n\nContent:\n{page_text}")
        url_context = "\n\n---\n\n".join(fetched_pages)

    # Build prompt
    system_prompt = get_system_prompt()
    if url_context:
        # Inject URL content into the user message
        query_with_context = f"{request.query}\n\n---\nHere is the content from the URL(s) mentioned above. Analyze this as part of your response:\n\n{url_context}"
        user_message = build_user_message(query_with_context, request.mode, chunks)
    else:
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

    # Persist to chat history (best-effort)
    conversation_id = None
    try:
        conversation_id = _persist_turn(
            username=user,
            conversation_id=request.conversation_id,
            user_content=request.query,
            assistant_content=response_text or "",
            mode=request.mode,
            sources=[s.model_dump() for s in sources],
            file_meta=None,
        )
    except Exception as e:
        print(f"chat persistence (query) failed: {e}")

    return QueryResponse(
        response=response_text,
        sources=sources,
        mode=request.mode,
        query=request.query,
        conversation_id=conversation_id,
    )


# ----- chat history helpers + endpoints -----

def _persist_turn(username: str,
                  conversation_id: Optional[str],
                  user_content: str,
                  assistant_content: str,
                  mode: Optional[str],
                  sources: Optional[list],
                  file_meta: Optional[dict]) -> str:
    """Persist a user+assistant pair. Creates the conversation if needed.
    Returns the conversation_id used."""
    is_new = False
    if conversation_id:
        existing = chats_db.get_conversation(username, conversation_id)
        if not existing:
            conversation_id = chats_db.create_conversation(username)["id"]
            is_new = True
    else:
        conversation_id = chats_db.create_conversation(username)["id"]
        is_new = True

    chats_db.add_message(conversation_id, "user", user_content, mode=mode, file_meta=file_meta)
    chats_db.add_message(conversation_id, "assistant", assistant_content, mode=mode, sources=sources)

    if is_new:
        chats_db.maybe_autotitle(username, conversation_id, user_content)
    return conversation_id


@app.get("/conversations")
async def list_convs(request: Request, q: Optional[str] = None):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    if q:
        return {"results": chats_db.search(user, q, limit=50), "query": q}
    return {"conversations": chats_db.list_conversations(user)}


@app.post("/conversations")
async def create_conv(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        body = await request.json()
    except Exception:
        body = {}
    title = (body or {}).get("title") or "New chat"
    return chats_db.create_conversation(user, title=str(title)[:80])


@app.get("/conversations/{conv_id}")
async def get_conv(conv_id: str, request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    conv = chats_db.get_conversation(user, conv_id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conv


@app.patch("/conversations/{conv_id}")
async def patch_conv(conv_id: str, request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        body = await request.json()
    except Exception:
        body = {}
    title = body.get("title")
    pinned = body.get("pinned")
    if title is not None:
        title = str(title)[:120]
    if pinned is not None:
        pinned = bool(pinned)
    conv = chats_db.update_conversation(user, conv_id, title=title, pinned=pinned)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conv


@app.delete("/conversations/{conv_id}")
async def del_conv(conv_id: str, request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    ok = chats_db.delete_conversation(user, conv_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return {"ok": True}

