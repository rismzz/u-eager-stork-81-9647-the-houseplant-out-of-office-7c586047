#!/usr/bin/env python3
"""The Houseplant Out-of-Office — writes one line to /output/entry.txt.

The funniest out-of-office auto-reply a houseplant would send, 120 characters
or fewer: it is away photosynthesizing and will reply after sun, water, and
gossip from the ficus — the plant world's version of "I'll circle back". Setup and punchline on a single line, in the voice of
an office auto-reply. Deterministic: no network, no randomness, no clock; the
line is embedded below as a literal and written verbatim.
"""

import os
from pathlib import Path

TEXT = (
    "I'm out of the office, photosynthesizing. I'll reply after sun, water, "
    "and gossip from the ficus."
)

MAX_CHARS = 120


def main() -> None:
    # Gate mirrors the sealed scorer: 1 to 120 characters, not only whitespace.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"text is {len(TEXT)} characters"
    assert TEXT.strip(), "text must not be only whitespace"
    assert "\n" not in TEXT, "text must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out = out_dir / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
