"""
Growthwick RAG Indexer
Run: python index.py

Chunks the corpus, generates embeddings, stores in SQLite (local) or pgvector (production).
"""

import os
import re
import json
import hashlib
import sqlite3
import pickle
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import numpy as np

# Token counting — use word-based estimate for speed (tiktoken is slow on 700 files)
def count_tokens(text: str) -> int:
    # Rough estimate: ~0.75 tokens per word for English prose
    return int(len(text.split()) * 0.75)

CORPUS_PATH = Path(os.getenv("CORPUS_PATH", str(Path(__file__).parent.parent / "corpus")))
DB_PATH = Path(__file__).parent / "growthwick.db"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SKIP_EMBEDDINGS = os.getenv("SKIP_EMBEDDINGS", "").lower() in ("1", "true", "yes")
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIM = 1536

# Token thresholds
MIN_CHUNK_TOKENS = 100
MAX_CHUNK_TOKENS = 1200
TARGET_CHUNK_TOKENS = 600
OVERLAP_TOKENS = 150


def get_source_url(content: str, file_path: Path) -> str:
    """Extract Source: URL from file content, fallback to filename."""
    match = re.search(r'^Source:\s*(https?://\S+)', content, re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return f"file://{file_path.name}"


def get_persona(file_path: Path) -> str:
    """Determine persona from file path."""
    parts = file_path.parts
    corpus_idx = None
    for i, part in enumerate(parts):
        if part == "corpus":
            corpus_idx = i
            break
    if corpus_idx is not None and len(parts) > corpus_idx + 1:
        return parts[corpus_idx + 1]
    return "unknown"


def get_type(file_path: Path) -> str:
    """Determine content type from path."""
    path_str = str(file_path).lower()
    if "transcripts" in path_str:
        if "lenny" in path_str:
            return "transcript"
        return "podcast"
    if "books" in path_str:
        return "book"
    return "article"


def split_by_headers(content: str) -> List[str]:
    """Split markdown content by H2/H3 headers."""
    # Split on ## or ### headers
    sections = re.split(r'\n(?=#{2,3}\s)', content)
    return [s.strip() for s in sections if s.strip()]


def split_by_paragraphs(text: str, target_tokens: int, overlap_tokens: int) -> List[str]:
    """Split text into chunks at paragraph boundaries."""
    paragraphs = re.split(r'\n{2,}', text)
    chunks = []
    current = []
    current_tokens = 0

    for para in paragraphs:
        para_tokens = count_tokens(para)
        if current_tokens + para_tokens > target_tokens and current:
            chunk_text = "\n\n".join(current)
            chunks.append(chunk_text)
            # Overlap: keep last paragraph(s) up to overlap_tokens
            overlap = []
            overlap_count = 0
            for p in reversed(current):
                pt = count_tokens(p)
                if overlap_count + pt <= overlap_tokens:
                    overlap.insert(0, p)
                    overlap_count += pt
                else:
                    break
            current = overlap
            current_tokens = overlap_count
        current.append(para)
        current_tokens += para_tokens

    if current:
        chunks.append("\n\n".join(current))

    return chunks


MAX_FILE_CHARS = 150_000  # Skip files larger than ~150KB (Lenny transcripts get chunked specially)


def simple_char_chunks(content: str, chunk_size: int = 3000, overlap: int = 400) -> List[str]:
    """Simple fixed-character chunking for large transcripts. Fast and predictable."""
    chunks = []
    start = 0
    while start < len(content):
        end = start + chunk_size
        # Try to break at a newline
        if end < len(content):
            newline = content.rfind('\n', start + chunk_size // 2, end)
            if newline > start:
                end = newline
        chunk = content[start:end].strip()
        if len(chunk) > 200:  # min meaningful chunk
            chunks.append(chunk)
        start = end - overlap
        if start >= len(content):
            break
    return chunks


def chunk_document(content: str, file_path: Path) -> List[Dict]:
    """Chunk a document into pieces with metadata."""
    doc_type = get_type(file_path)
    chunks = []

    if doc_type == "podcast":
        # Podcast RSS episodes: keep whole (they're short)
        if len(content) >= 200:
            chunks.append({"text": content[:5000], "chunk_index": 0})  # cap at 5000 chars
        return chunks

    if doc_type == "transcript":
        # Large transcripts: simple char-based chunking (much faster than paragraph splitting)
        parts = simple_char_chunks(content, chunk_size=3000, overlap=400)
        for i, part in enumerate(parts):
            chunks.append({"text": part, "chunk_index": i})
        return chunks

    # Articles and books: header-based chunking
    # If file is very large, fall back to char chunking
    if len(content) > MAX_FILE_CHARS:
        parts = simple_char_chunks(content, chunk_size=3000, overlap=400)
        for i, part in enumerate(parts):
            chunks.append({"text": part, "chunk_index": i})
        return chunks

    sections = split_by_headers(content)
    chunk_index = 0

    for section in sections:
        tokens = count_tokens(section)
        if tokens < MIN_CHUNK_TOKENS:
            continue
        elif tokens <= MAX_CHUNK_TOKENS:
            chunks.append({"text": section, "chunk_index": chunk_index})
            chunk_index += 1
        else:
            # Split large sections at paragraph breaks
            sub_chunks = split_by_paragraphs(section, TARGET_CHUNK_TOKENS, OVERLAP_TOKENS)
            for sub in sub_chunks:
                if count_tokens(sub) >= MIN_CHUNK_TOKENS:
                    chunks.append({"text": sub, "chunk_index": chunk_index})
                    chunk_index += 1

    return chunks


def file_hash(file_path: Path) -> str:
    """MD5 hash of file contents for change detection."""
    try:
        return hashlib.md5(file_path.read_bytes()).hexdigest()
    except Exception:
        return ""


def init_db(conn: sqlite3.Connection):
    """Initialize SQLite database schema."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona TEXT NOT NULL,
            file_name TEXT NOT NULL,
            file_hash TEXT NOT NULL,
            source_url TEXT NOT NULL,
            chunk_index INTEGER NOT NULL,
            type TEXT NOT NULL,
            chunk_text TEXT NOT NULL,
            embedding BLOB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_persona ON chunks(persona)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_type ON chunks(type)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_file_hash ON chunks(file_hash)")
    conn.commit()


def get_indexed_hashes(conn: sqlite3.Connection) -> set:
    """Get set of already-indexed file hashes."""
    cursor = conn.execute("SELECT DISTINCT file_hash FROM chunks")
    return {row[0] for row in cursor.fetchall()}


def embed_texts(texts: List[str], api_key: str) -> List[List[float]]:
    """Batch embed texts using OpenAI."""
    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    # Batch in groups of 100
    all_embeddings = []
    batch_size = 100
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=batch
        )
        all_embeddings.extend([e.embedding for e in response.data])
    return all_embeddings


def index_corpus(force_reindex: bool = False):
    """Main indexing function."""
    print(f"Corpus path: {CORPUS_PATH}")
    if not CORPUS_PATH.exists():
        print(f"ERROR: Corpus path does not exist: {CORPUS_PATH}")
        return

    conn = sqlite3.connect(str(DB_PATH))
    init_db(conn)

    indexed_hashes = get_indexed_hashes(conn) if not force_reindex else set()
    if force_reindex:
        conn.execute("DELETE FROM chunks")
        conn.commit()
        print("Force reindex: cleared existing chunks")

    # Find all markdown files
    md_files = list(CORPUS_PATH.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")

    total_chunks = 0
    skipped = 0
    errors = 0

    print(f"Processing {len(md_files)} files...")
    for file_idx, file_path in enumerate(md_files):
        if file_idx % 50 == 0:
            print(f"  Progress: {file_idx}/{len(md_files)} files...")

        fhash = file_hash(file_path)
        if fhash in indexed_hashes:
            skipped += 1
            continue

        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  ERROR reading {file_path.name}: {e}")
            errors += 1
            continue

        persona = get_persona(file_path)
        source_url = get_source_url(content, file_path)
        doc_type = get_type(file_path)

        chunks = chunk_document(content, file_path)
        if not chunks:
            continue

        # Embed all chunks for this file
        texts = [c["text"] for c in chunks]
        try:
            if OPENAI_API_KEY and not SKIP_EMBEDDINGS:
                embeddings = embed_texts(texts, OPENAI_API_KEY)
            else:
                # No embedding — BM25 still works fully
                embeddings = [None for _ in texts]
        except Exception as e:
            print(f"  ERROR embedding {file_path.name}: {e}")
            errors += 1
            continue

        # Store chunks
        for chunk, embedding in zip(chunks, embeddings):
            emb_blob = pickle.dumps(np.array(embedding, dtype=np.float32)) if embedding is not None else None
            conn.execute(
                """INSERT INTO chunks (persona, file_name, file_hash, source_url, chunk_index, type, chunk_text, embedding)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (persona, file_path.name, fhash, source_url, chunk["chunk_index"],
                 doc_type, chunk["text"], emb_blob)
            )
            total_chunks += 1

        conn.commit()
        indexed_hashes.add(fhash)

    print(f"\n=== INDEXING COMPLETE ===")
    print(f"New chunks indexed: {total_chunks}")
    print(f"Files skipped (already indexed): {skipped}")
    print(f"Errors: {errors}")

    # Stats
    cursor = conn.execute("SELECT COUNT(*), COUNT(DISTINCT persona) FROM chunks")
    total, personas = cursor.fetchone()
    print(f"Total chunks in DB: {total} across {personas} personas")

    conn.close()


if __name__ == "__main__":
    import sys
    force = "--force" in sys.argv
    if "--no-embed" in sys.argv:
        import builtins
        # Monkeypatch to skip embeddings
        orig_get = os.getenv
        os.environ["SKIP_EMBEDDINGS"] = "1"

    if SKIP_EMBEDDINGS or "--no-embed" in sys.argv:
        print("BM25-only mode: skipping embeddings (fast indexing)")
    elif OPENAI_API_KEY:
        print(f"Embedding mode: {EMBEDDING_MODEL}")
    else:
        print("No API key: BM25-only mode")

    index_corpus(force_reindex=force)
