#!/usr/bin/env python3
"""One Line to Your Younger Self -- make.fun entry.

Writes a single line, in English, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; fully deterministic: the same line every run.
"""

import os

LINE = (
    "Kid, stop apologizing for your accent — one day people will pay "
    "to hear the boy from Batang tell them where home is."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
