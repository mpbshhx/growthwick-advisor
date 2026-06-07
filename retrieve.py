"""
Growthwick RAG Retriever
Hybrid search: semantic (embedding cosine similarity) + BM25 keyword search
Fusion: Reciprocal Rank Fusion (RRF)
"""

import os
import re
import sqlite3
import pickle
import numpy as np
from pathlib import Path
from typing import List, Dict, Optional, Tuple

from rank_bm25 import BM25Okapi

DB_PATH = Path(__file__).parent / "growthwick.db"

# RRF constant
RRF_K = 60
TOP_N = 6  # final chunks to return


# Expert name → persona directory mapping
EXPERT_MAP = {
    "roetzer": "roetzer",
    "paul roetzer": "roetzer",
    "neil patel": "patel",
    "patel": "patel",
    "chris walker": "walker",
    "walker": "walker",
    "rand fishkin": "fishkin",
    "fishkin": "fishkin",
    "lenny": "lenny",
    "lenny rachitsky": "lenny",
    "emily kramer": "emily-kramer",
    "kramer": "emily-kramer",
    "kyle poyar": "kyle-poyar",
    "poyar": "kyle-poyar",
    "brian balfour": "brian-balfour",
    "balfour": "brian-balfour",
    "kieran flanagan": "kieran-flanagan",
    "flanagan": "kieran-flanagan",
    "dharmesh": "dharmesh-shah",
    "dharmesh shah": "dharmesh-shah",
    "elena verna": "elena-verna",
    "elena": "elena-verna",
    "april dunford": "april-dunford",
    "dunford": "april-dunford",
    "peep laja": "peep-laja",
    "laja": "peep-laja",
    "wes bush": "wes-bush",
    "bush": "wes-bush",
    "joanna wiebe": "joanna-wiebe",
    "wiebe": "joanna-wiebe",
    "dave gerhardt": "dave-gerhardt",
    "gerhardt": "dave-gerhardt",
}


def detect_persona_filter(query: str) -> Optional[str]:
    """Auto-detect if the query mentions a specific expert."""
    q_lower = query.lower()
    for name, persona in EXPERT_MAP.items():
        if name in q_lower:
            return persona
    return None


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


class Retriever:
    def __init__(self):
        self.conn = None
        self.bm25 = None
        self.bm25_chunks = []  # parallel list of chunk rows
        self._load()

    def _load(self):
        """Load DB connection and build BM25 index."""
        if not DB_PATH.exists():
            print(f"WARNING: Database not found at {DB_PATH}. Run python index.py first.")
            return

        self.conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

        # Build BM25 index from all chunks
        cursor = self.conn.execute(
            "SELECT id, persona, file_name, source_url, chunk_index, type, chunk_text FROM chunks"
        )
        rows = cursor.fetchall()
        if not rows:
            print("WARNING: No chunks in database. Run python index.py first.")
            return

        self.bm25_chunks = rows
        tokenized = [self._tokenize(row["chunk_text"]) for row in rows]
        self.bm25 = BM25Okapi(tokenized)
        print(f"Retriever loaded: {len(rows)} chunks, BM25 index built")

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization for BM25."""
        text = text.lower()
        tokens = re.findall(r'\b[a-z0-9]+(?:-[a-z0-9]+)*\b', text)
        return tokens

    def semantic_search(self, query_embedding: np.ndarray,
                       persona_filter: Optional[str] = None,
                       top_k: int = 10) -> List[Tuple[int, float]]:
        """Semantic search using cosine similarity. Returns list of (row_id, score)."""
        if self.conn is None:
            return []

        where = ""
        params = []
        if persona_filter:
            where = "WHERE persona = ?"
            params.append(persona_filter)

        cursor = self.conn.execute(
            f"SELECT id, embedding FROM chunks {where}", params
        )
        rows = cursor.fetchall()

        scores = []
        for row in rows:
            if row["embedding"] is None:
                continue
            emb = pickle.loads(row["embedding"])
            sim = cosine_similarity(query_embedding, emb)
            scores.append((row["id"], sim))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

    def bm25_search(self, query: str,
                    persona_filter: Optional[str] = None,
                    top_k: int = 10) -> List[Tuple[int, float]]:
        """BM25 keyword search. Returns list of (row_id, score)."""
        if self.bm25 is None:
            return []

        tokens = self._tokenize(query)
        scores = self.bm25.get_scores(tokens)

        results = []
        for i, (chunk, score) in enumerate(zip(self.bm25_chunks, scores)):
            if persona_filter and chunk["persona"] != persona_filter:
                continue
            if score > 0:
                results.append((chunk["id"], score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

    def rrf_fusion(self, semantic_results: List[Tuple[int, float]],
                   bm25_results: List[Tuple[int, float]]) -> List[Tuple[int, float]]:
        """Reciprocal Rank Fusion of two ranked lists."""
        scores: Dict[int, float] = {}

        for rank, (doc_id, _) in enumerate(semantic_results):
            scores[doc_id] = scores.get(doc_id, 0) + 1.0 / (rank + 1 + RRF_K)

        for rank, (doc_id, _) in enumerate(bm25_results):
            scores[doc_id] = scores.get(doc_id, 0) + 1.0 / (rank + 1 + RRF_K)

        fused = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return fused

    def get_chunks_by_ids(self, ids: List[int]) -> List[Dict]:
        """Fetch full chunk data by IDs."""
        if not ids or self.conn is None:
            return []
        placeholders = ",".join("?" * len(ids))
        cursor = self.conn.execute(
            f"SELECT id, persona, file_name, source_url, chunk_index, type, chunk_text FROM chunks WHERE id IN ({placeholders})",
            ids
        )
        rows = cursor.fetchall()
        # Preserve order from ids
        row_map = {row["id"]: row for row in rows}
        return [dict(row_map[i]) for i in ids if i in row_map]

    def retrieve(self, query: str,
                 query_embedding: Optional[np.ndarray] = None,
                 persona_filter: Optional[str] = None) -> List[Dict]:
        """Main retrieval: hybrid search + RRF fusion, returns top chunks."""
        if self.conn is None:
            return []

        # Auto-detect persona filter if not provided
        if persona_filter is None:
            persona_filter = detect_persona_filter(query)

        # Semantic search
        semantic_results = []
        if query_embedding is not None:
            semantic_results = self.semantic_search(query_embedding, persona_filter, top_k=10)

        # BM25 search
        bm25_results = self.bm25_search(query, persona_filter, top_k=10)

        # If no semantic results, fall back to BM25 only
        if not semantic_results and bm25_results:
            top_ids = [doc_id for doc_id, _ in bm25_results[:TOP_N]]
            return self.get_chunks_by_ids(top_ids)

        # If no BM25 results, use semantic only
        if not bm25_results and semantic_results:
            top_ids = [doc_id for doc_id, _ in semantic_results[:TOP_N]]
            return self.get_chunks_by_ids(top_ids)

        # Fuse results
        fused = self.rrf_fusion(semantic_results, bm25_results)
        top_ids = [doc_id for doc_id, _ in fused[:TOP_N]]
        return self.get_chunks_by_ids(top_ids)

    def get_stats(self) -> Dict:
        """Return corpus statistics."""
        if self.conn is None:
            return {"total_chunks": 0, "personas": 0}
        cursor = self.conn.execute(
            "SELECT COUNT(*), COUNT(DISTINCT persona) FROM chunks"
        )
        total, personas = cursor.fetchone()
        return {"total_chunks": total, "personas": personas}

    def get_personas(self) -> List[Dict]:
        """Return list of personas with chunk and file counts."""
        if self.conn is None:
            return []
        cursor = self.conn.execute(
            "SELECT persona, COUNT(*) as chunk_count, COUNT(DISTINCT file_name) as file_count FROM chunks GROUP BY persona ORDER BY chunk_count DESC"
        )
        return [{"persona": row[0], "chunk_count": row[1], "file_count": row[2]} for row in cursor.fetchall()]


# Singleton retriever (built once at startup)
_retriever: Optional[Retriever] = None


def get_retriever() -> Retriever:
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever
