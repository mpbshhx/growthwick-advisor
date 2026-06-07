"""
Growthwick prompt assembly.
Reads system prompt from SYSTEM-PROMPT.md, injects retrieved chunks as context.
"""

import os
from pathlib import Path
from typing import List, Dict

SYSTEM_PROMPT_PATH = Path(__file__).parent.parent / "SYSTEM-PROMPT.md"


def load_system_prompt() -> str:
    """Load the system prompt from file."""
    try:
        return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
    except Exception:
        return "You are the Growthwick Marketing Advisor. Help the user with their marketing strategy using evidence-backed advice."


def format_chunks_as_context(chunks: List[Dict]) -> str:
    """Format retrieved chunks as context block for injection."""
    if not chunks:
        return ""

    lines = ["## RETRIEVED CONTEXT\n"]
    lines.append("The following passages are from the expert corpus. Use these as the basis for your response. Only cite sources present here.\n")

    for i, chunk in enumerate(chunks, 1):
        persona = chunk.get("persona", "unknown")
        source_url = chunk.get("source_url", "")
        file_name = chunk.get("file_name", "")
        chunk_text = chunk.get("chunk_text", "")

        lines.append(f"### Source {i}: [{persona}] {file_name}")
        if source_url and not source_url.startswith("file://"):
            lines.append(f"URL: {source_url}")
        lines.append("")
        lines.append(chunk_text[:2000])  # cap per chunk to stay in context budget
        lines.append("")

    lines.append("---")
    lines.append("CITATION RULE: Only cite the sources above. If the retrieved content does not directly address the question, say so explicitly before answering. Do not paraphrase retrieved content as direct quotes — describe the concept and cite the source.")
    lines.append("")

    return "\n".join(lines)


def build_user_message(query: str, mode: str, chunks: List[Dict]) -> str:
    """Build the full user message with retrieved context."""
    context = format_chunks_as_context(chunks)

    mode_instruction = ""
    if mode == "stress-test":
        mode_instruction = "\n**MODE: STRESS-TEST** — I am submitting a plan/strategy for adversarial review. Challenge my assumptions, identify weaknesses, invoke relevant experts by name.\n"
    elif mode == "strategy-build":
        mode_instruction = "\n**MODE: STRATEGY BUILD** — I need help building or improving a marketing strategy. Diagnose the situation, recommend frameworks, give concrete execution steps.\n"

    return f"{context}\n{mode_instruction}\n{query}"


def get_system_prompt() -> str:
    return load_system_prompt()
