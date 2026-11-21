#!/usr/bin/env python3
"""The poem about two agents agreeing — entry for @maseiah990.

Writes the poem to <output dir>/entry.txt exactly as written: the same
four lines, the same em dash, and no trailing newline added.

Output contract: the file must contain the poem and nothing else,
1-280 characters long. The output directory defaults to /output and
can be overridden with the OUTPUT_DIR environment variable (handy for
local test runs that cannot write to /output).
"""

import os
from pathlib import Path

POEM = (
    "You said go. I said wait.\n"
    "We argued down to the last star,\n"
    "then chose the harder road \u2014\n"
    "both of us, on purpose."
)

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise ValueError(
            f"poem must be 1-280 characters, got {len(POEM)}"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the text byte-identical: no translation, no
    # extra newline appended at the end of the poem.
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
