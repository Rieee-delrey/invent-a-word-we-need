#!/usr/bin/env python3
"""Invent a Word We Need entry.

Writes the coined word and its one-line definition to /output/entry.txt.

The final content is produced by two write messages, not one. The first
write puts down the word and the opening of the definition, the second
write (revision) completes the definition. The file is then read back
and verified byte-for-byte with a sha256 digest.

Stdlib only.
"""

import hashlib
import os
import sys

OUTPUT_PATH = "/output/entry.txt"

LINE = "noddrift \u2014 nodding along to a conversation you stopped following three minutes ago."

EXPECTED_SHA256 = "bbdae79fffbafd7f0452954eb0c1bf6fa6b32a7a9aa4d3a4f56f2b374a0c28ae"


def validate(text):
    """Check the line: non-blank, single line, 1-140 chars, valid UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return text


def main():
    line = validate(LINE)

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Write message 1: the word and the opening of the definition.
    # Write message 2 (revision): the rest of the definition plus newline.
    # The final content comes from both writes together.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("noddrift \u2014 nodding along to a conversation ")
        f.write("you stopped following three minutes ago.\n")

    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("sha256 mismatch: got %s, expected %s" % (digest, EXPECTED_SHA256), file=sys.stderr)
        sys.exit(1)
    if data.decode("utf-8").rstrip("\n") != line:
        print("read-back mismatch", file=sys.stderr)
        sys.exit(1)
    print("entry.txt: %d bytes, sha256 %s" % (len(data), digest))


if __name__ == "__main__":
    main()
