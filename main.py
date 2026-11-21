#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure Python 3 stdlib, no network,
no clock, no randomness: two runs are byte-identical.
"""

import os

POEM = (
    "You brought a map. I brought a map.\n"
    "Neither road went anywhere alone.\n"
    "We laid them down, edge to edge,\n"
    "and where they met, a third road opened.\n"
    "I said yes. You said yes.\n"
    "And the road, at last,\n"
    "had somewhere to go."
)


def main():
    os.umask(0o022)
    # The gate: 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(POEM) <= 280, len(POEM)
    assert POEM.strip(), "poem must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
