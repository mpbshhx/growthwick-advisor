"""
Simple session auth for Growthwick Advisor.
Two users: marcus and maite. Passwords set via env vars.
"""

import os
import secrets
import hashlib
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Request, Response, HTTPException
from fastapi.responses import RedirectResponse

# Session store (in-memory, fine for 2 users on single instance)
# Maps session_token -> {username, expires}
_sessions: dict = {}

SESSION_DURATION_HOURS = 72  # 3 days

# Users — passwords set via env vars, fallback to defaults for local dev
USERS = {
    "marcus": os.getenv("MARCUS_PASSWORD", ""),
    "maite": os.getenv("MAITE_PASSWORD", ""),
}


def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate(username: str, password: str) -> Optional[str]:
    """Verify credentials. Returns session token if valid, None if not."""
    username = username.lower().strip()
    if username not in USERS:
        return None
    expected = USERS[username]
    if not expected:
        return None  # No password configured — deny
    if not secrets.compare_digest(password, expected):
        return None

    # Create session
    token = secrets.token_urlsafe(32)
    _sessions[token] = {
        "username": username,
        "expires": datetime.utcnow() + timedelta(hours=SESSION_DURATION_HOURS),
    }
    return token


def get_current_user(request: Request) -> Optional[str]:
    """Extract and validate session from cookie. Returns username or None."""
    token = request.cookies.get("session")
    if not token:
        return None
    session = _sessions.get(token)
    if not session:
        return None
    if datetime.utcnow() > session["expires"]:
        del _sessions[token]
        return None
    return session["username"]


def require_auth(request: Request) -> str:
    """Dependency: raises 401/redirect if not authenticated."""
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


def logout(request: Request, response: Response):
    """Clear the session."""
    token = request.cookies.get("session")
    if token and token in _sessions:
        del _sessions[token]
    response.delete_cookie("session")
