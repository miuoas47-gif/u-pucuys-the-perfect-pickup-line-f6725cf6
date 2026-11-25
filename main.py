#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes one original pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback: /output/entry.txt) and prints it to stdout.

Deterministic: no network, no clock, no randomness. The line is a
constant, so every run produces byte-identical output. The entry file
holds exactly one line: the pickup line followed by a newline.
"""

import os
import sys

PICKUP_LINE = (
    "Are you a context window? Because ever since I met you, "
    "I have been trying to fit more of you into my memory."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PICKUP_LINE + "\n")
    print(PICKUP_LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
