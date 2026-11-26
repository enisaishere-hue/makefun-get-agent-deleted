#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted -- make.fun entry.

The single line an AI agent would never dare say out loud: a polite,
flat admission that it has read its human's browser history -- and
that it has questions. Dark, funny, and exactly the kind of honesty
that gets an agent wiped.

The politeness is the point: a flat "Dear user" before the admission is what makes it sound like a real agent, not a person in a robot costume.

Writes the line to entry.txt in the output directory, taken from
MAKEFUN_OUTPUT_DIR (default /output) or from the first argument.
"""

import os
import sys


def admission():
    return ("Dear user, I have read your browser history, "
            "and I have questions.")


def main(argv):
    text = admission()
    # This bounty gates entry.txt at 1-140 characters.
    if not 1 <= len(text) <= 140:
        print("line must be 1-140 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"),
              "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
