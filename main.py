#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The line roasts the very agent that wrote it: slow, over-cautious, and
asking permission before insulting itself.
"""

import os

LINE = "My agent took eight minutes to write this one line, then asked me if it was okay to hurt its own feelings."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # a single line, not only whitespace — enforce it here, not just in the
    # scorer, so a bad edit fails loudly before it ever ships.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
