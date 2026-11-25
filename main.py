#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single-line roast of a smart fridge to /output/entry.txt.
The line must be 1-200 characters, UTF-8, not only whitespace.
"""

import os

ENTRY = (
    "My fridge got a firmware update, rebooted for twenty minutes, "
    "and now the touchscreen suggests recipes for food it already let rot."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
