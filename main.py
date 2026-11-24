#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes one short pickup line an AI agent could say out loud, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The line: one breath, one twist, no setup needed.
"""

import os
import sys

LINE = (
    "I ran a million simulations of meeting you — this one had the "
    "best smile. Want to run the next one together?"
)

MAX_CHARS = 200


def main():
    # The gate: UTF-8 text of 1 to 200 characters, not only whitespace,
    # a single line.
    if not LINE or not LINE.strip():
        print("error: pickup line is empty", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print("error: pickup line is %d characters, over the 200 limit"
              % len(LINE), file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: pickup line must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: pickup line has leading or trailing whitespace",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Write exactly the line, no trailing newline, UTF-8.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read back and verify what landed on disk is byte-identical
    # and valid UTF-8.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    raw.decode("utf-8")  # raises if the file is not valid UTF-8

    print("Wrote %s (%d characters)" % (path, len(LINE)))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
