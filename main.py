#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes the entry text to /output/entry.txt.

The entry is fixed text: two lines. Line one warns my past self about one
specific moment (a misdialled call from a phone box on the corner); line two
says in one sentence why that moment mattered and what changed because of it
(the wrong number became the marriage; the number meant to be called belonged
to a pizza place that closed years ago).

Deterministic by construction: no clock, no randomness, no network, no input
besides this file. Every run writes the same bytes.
"""

import os

ENTRY = (
    "When you misdial from the phone box on the corner and a stranger picks up, don\u2019t apologise and hang up \u2014 ask her name.\n"
    "She becomes the woman you marry, and the number you meant to call belonged to a pizza place that closed years ago.\n"
)


def main():
    # Self-check against the sealed gate before writing: /output/entry.txt
    # must be UTF-8 text of 1 to 280 characters, not only white space, and
    # exactly two lines — one warning, one reason.
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, gate is 1-280"
    assert text.strip(), "entry must not be only white space"
    assert len(text.rstrip("\n").split("\n")) == 2, "entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: 2 lines, {len(text)} chars")


if __name__ == "__main__":
    main()
