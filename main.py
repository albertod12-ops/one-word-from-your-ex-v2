#!/usr/bin/env python3
"""One Word From Your Ex — v2.

Writes exactly one word to /output/entry.txt: the word an ex would use to
describe you. "Used" lands twice in four letters — you were used goods,
and you used her. The ex's whole verdict, no explanation needed.
"""

import os

os.umask(0o022)

WORD = "Used"


def main():
    words = WORD.split()
    assert len(words) == 1, "entry must be exactly one word, got %d" % len(words)
    assert "\n" not in WORD, "entry must be a single line"
    assert 1 <= len(WORD.encode("utf-8")) <= 24, "entry must be 1-24 characters"
    assert WORD.strip() == WORD and WORD, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
