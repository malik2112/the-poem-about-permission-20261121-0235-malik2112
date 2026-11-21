#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about permission to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem is "The Stairs": a son asks to take his father's arm,
is refused, and is given a different role instead — to walk
close behind, hands empty, ready but not touching. Agency here
is the help that stays near without taking over.
"""

import os

TEXT = (
    "The Stairs\n"
    "\n"
    "May I take your arm?\n"
    "Dad shook his head.\n"
    "Just walk behind me,\n"
    "he said. Close.\n"
    "\n"
    "So I climbed below him,\n"
    "both hands empty,\n"
    "ready, not touching,\n"
    "while he pulled himself up\n"
    "rail by rail —\n"
    "his stairs, his pace,\n"
    "my nearness the help."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
