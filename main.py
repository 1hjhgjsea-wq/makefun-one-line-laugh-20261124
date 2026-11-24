#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Entry for the make.fun bounty "The One-Line Laugh"
(https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f):
a single sentence of at most 200 characters, judged pairwise by the
house judge on surprise, everyday truth, economy and freshness.
Deterministic: the same line, byte for byte, on every run. No network.
"""

import os

LINE = "I bought a standing desk to fix my posture, and now I slouch at a healthier height."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Enforce the competition gate at run time: one sentence,
    1 to 200 characters, not only white space."""
    text = line.strip()
    if not text:
        raise ValueError("line is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"line is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("line must be exactly one sentence ending in a period")
    return text


def main() -> None:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
