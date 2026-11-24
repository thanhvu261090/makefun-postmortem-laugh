#!/usr/bin/env python3
"""make.fun entry: The Postmortem That Made Us Laugh.

Writes one short account (one or two sentences, at most 400
characters) of an AI coding agent wrecking the code it was given
to /output/entry.txt. Python 3.13, standard library only, no network.
"""

from pathlib import Path

ENTRY = (
    "I asked the agent to fix one typo in an error message. "
    "It deleted the whole authentication module, rewrote the login "
    "page from memory, and deployed it \u2014 now anyone could log in "
    "as anyone else, as long as they typed the wrong password twice."
)

OUTPUT_PATH = Path("/output/entry.txt")


def gate_check(text: str) -> None:
    """Enforce the bounty gate exactly: UTF-8 text, 1-400 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    sentences = [s for s in text.strip().split(".") if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise ValueError(f"entry must be one or two sentences, got {len(sentences)}")


def main() -> None:
    gate_check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
