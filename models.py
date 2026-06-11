from pydantic import BaseModel
from typing import Optional, List


class QueryRequest(BaseModel):
    query: str
    mode: str = "strategy-build"  # "stress-test" | "strategy-build"
    persona_filter: Optional[str] = None
    conversation_id: Optional[str] = None


class ChunkSource(BaseModel):
    persona: str
    file_name: str
    source_url: str
    chunk_index: int
    type: str
    text: str  # raw chunk text for verification


class QueryResponse(BaseModel):
    response: str
    sources: List[ChunkSource]
    mode: str
    query: str
    conversation_id: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    total_chunks: int
    personas: int
    corpus_path: str


class PersonaInfo(BaseModel):
    persona: str
    chunk_count: int
    file_count: int
