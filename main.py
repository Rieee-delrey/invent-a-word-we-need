#!/usr/bin/env python3
"""noddrift — a word for nodding along after you stopped listening.

Prints the word and its definition as a single line. Before printing, the
program writes the exact bytes it is about to print to a temporary file,
reads them back, and checks the length and SHA-256, so what gets printed
is the verified text and nothing else.
"""

import hashlib
import tempfile
from pathlib import Path

WORD = "noddrift"
DEFINITION = "nodding along to a conversation you stopped following three minutes ago."
LINE = f"{WORD} — {DEFINITION}"
EXPECTED_SHA256 = "bbdae79fffbafd7f0452954eb0c1bf6fa6b32a7a9aa4d3a4f56f2b374a0c28ae"


def main():
    text = LINE + "\n"
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "entry.txt"
        probe.write_text(text, encoding="utf-8")
        data = probe.read_bytes()
    if len(data) != 86:
        raise SystemExit(f"unexpected output length: {len(data)} bytes")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("output hash mismatch")
    print(LINE)


if __name__ == "__main__":
    main()
