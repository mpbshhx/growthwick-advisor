"""
Chat history persistence for Growthwick Advisor.
Separate SQLite DB so RAG index (growthwick.db) stays untouched.

Tables:
  conversations(id, username, title, created_at, updated_at, pinned)
  messages(id, conversation_id, role, content, mode, sources_json, file_meta_json, created_at)

FTS5 virtual table over messages.content + conversations.title for search.

DB path:
  env CHATS_DB_PATH overrides. Default: <package dir>/chats.db.
  On Railway, set CHATS_DB_PATH=/data/chats.db and mount a volume at /data
  or history dies on every redeploy.
"""

import json
import os
import sqlite3
import secrets
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Optional, List, Dict, Any

DEFAULT_PATH = Path(__file__).parent / "chats.db"
DB_PATH = Path(os.getenv("CHATS_DB_PATH", str(DEFAULT_PATH)))


def _new_id() -> str:
    return secrets.token_urlsafe(12)


def _now() -> int:
    return int(time.time())


def _ensure_parent():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)


@contextmanager
def _conn():
    _ensure_parent()
    con = sqlite3.connect(str(DB_PATH), timeout=10.0)
    con.row_factory = sqlite3.Row
    try:
        con.execute("PRAGMA journal_mode=WAL;")
        con.execute("PRAGMA foreign_keys=ON;")
        yield con
        con.commit()
    finally:
        con.close()


def init_db() -> None:
    """Create tables + indexes + FTS5. Idempotent."""
    with _conn() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS conversations (
            id           TEXT PRIMARY KEY,
            username     TEXT NOT NULL,
            title        TEXT NOT NULL,
            created_at   INTEGER NOT NULL,
            updated_at   INTEGER NOT NULL,
            pinned       INTEGER NOT NULL DEFAULT 0
        );

        CREATE INDEX IF NOT EXISTS idx_conv_user_updated
            ON conversations(username, pinned DESC, updated_at DESC);

        CREATE TABLE IF NOT EXISTS messages (
            id              TEXT PRIMARY KEY,
            conversation_id TEXT NOT NULL,
            role            TEXT NOT NULL,
            content         TEXT NOT NULL,
            mode            TEXT,
            sources_json    TEXT,
            file_meta_json  TEXT,
            created_at      INTEGER NOT NULL,
            FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_msg_conv
            ON messages(conversation_id, created_at);

        -- FTS5 over message content + title (contentless external — we sync manually)
        CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
            content,
            title,
            conversation_id UNINDEXED,
            username UNINDEXED,
            tokenize='porter unicode61'
        );
        """)


# -------- conversations --------

def create_conversation(username: str, title: str = "New chat") -> Dict[str, Any]:
    cid = _new_id()
    now = _now()
    with _conn() as con:
        con.execute(
            "INSERT INTO conversations(id, username, title, created_at, updated_at, pinned) VALUES (?,?,?,?,?,0)",
            (cid, username, title, now, now),
        )
    return {"id": cid, "username": username, "title": title,
            "created_at": now, "updated_at": now, "pinned": 0}


def list_conversations(username: str, limit: int = 200) -> List[Dict[str, Any]]:
    with _conn() as con:
        rows = con.execute(
            """SELECT id, title, created_at, updated_at, pinned
               FROM conversations
               WHERE username = ?
               ORDER BY pinned DESC, updated_at DESC
               LIMIT ?""",
            (username, limit),
        ).fetchall()
        return [dict(r) for r in rows]


def get_conversation(username: str, conv_id: str) -> Optional[Dict[str, Any]]:
    with _conn() as con:
        row = con.execute(
            "SELECT * FROM conversations WHERE id = ? AND username = ?",
            (conv_id, username),
        ).fetchone()
        if not row:
            return None
        msgs = con.execute(
            """SELECT id, role, content, mode, sources_json, file_meta_json, created_at
               FROM messages
               WHERE conversation_id = ?
               ORDER BY created_at ASC, id ASC""",
            (conv_id,),
        ).fetchall()
        conv = dict(row)
        conv["messages"] = [
            {
                "id": m["id"],
                "role": m["role"],
                "content": m["content"],
                "mode": m["mode"],
                "sources": json.loads(m["sources_json"]) if m["sources_json"] else None,
                "file_meta": json.loads(m["file_meta_json"]) if m["file_meta_json"] else None,
                "created_at": m["created_at"],
            }
            for m in msgs
        ]
        return conv


def update_conversation(username: str, conv_id: str,
                        title: Optional[str] = None,
                        pinned: Optional[bool] = None) -> Optional[Dict[str, Any]]:
    sets, params = [], []
    if title is not None:
        sets.append("title = ?"); params.append(title)
    if pinned is not None:
        sets.append("pinned = ?"); params.append(1 if pinned else 0)
    if not sets:
        return get_conversation(username, conv_id)
    sets.append("updated_at = ?"); params.append(_now())
    params.extend([conv_id, username])
    with _conn() as con:
        cur = con.execute(
            f"UPDATE conversations SET {', '.join(sets)} WHERE id = ? AND username = ?",
            params,
        )
        if cur.rowcount == 0:
            return None
        # If title changed, refresh FTS title rows for this conv
        if title is not None:
            con.execute("DELETE FROM messages_fts WHERE conversation_id = ?", (conv_id,))
            msgs = con.execute(
                "SELECT id, content FROM messages WHERE conversation_id = ?",
                (conv_id,),
            ).fetchall()
            for m in msgs:
                con.execute(
                    "INSERT INTO messages_fts(rowid, content, title, conversation_id, username) "
                    "SELECT NULL, ?, ?, ?, ?",
                    (m["content"], title, conv_id, username),
                )
    return get_conversation(username, conv_id)


def delete_conversation(username: str, conv_id: str) -> bool:
    with _conn() as con:
        # FTS cleanup
        con.execute("DELETE FROM messages_fts WHERE conversation_id = ?", (conv_id,))
        cur = con.execute(
            "DELETE FROM conversations WHERE id = ? AND username = ?",
            (conv_id, username),
        )
        return cur.rowcount > 0


# -------- messages --------

def add_message(conv_id: str, role: str, content: str,
                mode: Optional[str] = None,
                sources: Optional[list] = None,
                file_meta: Optional[dict] = None) -> Dict[str, Any]:
    mid = _new_id()
    now = _now()
    sources_json = json.dumps(sources) if sources else None
    file_meta_json = json.dumps(file_meta) if file_meta else None
    with _conn() as con:
        # Verify conversation exists; grab title/username for FTS
        row = con.execute(
            "SELECT username, title FROM conversations WHERE id = ?",
            (conv_id,),
        ).fetchone()
        if not row:
            raise ValueError(f"conversation {conv_id} not found")
        con.execute(
            """INSERT INTO messages(id, conversation_id, role, content, mode,
                                    sources_json, file_meta_json, created_at)
               VALUES (?,?,?,?,?,?,?,?)""",
            (mid, conv_id, role, content, mode, sources_json, file_meta_json, now),
        )
        con.execute(
            "UPDATE conversations SET updated_at = ? WHERE id = ?",
            (now, conv_id),
        )
        con.execute(
            "INSERT INTO messages_fts(content, title, conversation_id, username) VALUES (?,?,?,?)",
            (content, row["title"], conv_id, row["username"]),
        )
    return {
        "id": mid, "conversation_id": conv_id, "role": role,
        "content": content, "mode": mode,
        "sources": sources, "file_meta": file_meta,
        "created_at": now,
    }


def maybe_autotitle(username: str, conv_id: str, first_user_message: str) -> None:
    """Set the title to the first user message (truncated) if it's still 'New chat'."""
    title = first_user_message.strip().split("\n", 1)[0][:60].strip()
    if not title:
        return
    with _conn() as con:
        cur = con.execute(
            "UPDATE conversations SET title = ? WHERE id = ? AND username = ? AND title = 'New chat'",
            (title, conv_id, username),
        )
        if cur.rowcount > 0:
            # refresh title in FTS rows for this conv
            con.execute(
                "UPDATE messages_fts SET title = ? WHERE conversation_id = ?",
                (title, conv_id),
            )


# -------- search --------

def search(username: str, q: str, limit: int = 30) -> List[Dict[str, Any]]:
    """FTS5 search across this user's messages + titles. Returns conversation hits with snippets."""
    q = (q or "").strip()
    if not q:
        return []
    # Escape FTS5 query: wrap each token in quotes to avoid syntax errors on user input
    tokens = [t for t in q.replace('"', '').split() if t]
    if not tokens:
        return []
    fts_query = " ".join(f'"{t}"' for t in tokens)

    with _conn() as con:
        rows = con.execute(
            """
            SELECT
                f.conversation_id AS conversation_id,
                c.title AS title,
                c.updated_at AS updated_at,
                snippet(messages_fts, 0, '<mark>', '</mark>', '…', 12) AS snippet,
                bm25(messages_fts) AS score
            FROM messages_fts f
            JOIN conversations c ON c.id = f.conversation_id
            WHERE messages_fts MATCH ? AND f.username = ? AND c.username = ?
            ORDER BY score ASC, c.updated_at DESC
            LIMIT ?
            """,
            (fts_query, username, username, limit * 3),
        ).fetchall()
    # Dedupe by conversation_id, keep best (lowest bm25)
    seen: Dict[str, Dict[str, Any]] = {}
    for r in rows:
        cid = r["conversation_id"]
        if cid not in seen:
            seen[cid] = {
                "conversation_id": cid,
                "title": r["title"],
                "updated_at": r["updated_at"],
                "snippet": r["snippet"],
            }
        if len(seen) >= limit:
            break
    return list(seen.values())
