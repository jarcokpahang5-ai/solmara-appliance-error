"""The Funniest Honest Appliance Error — make.fun entry.

Writes a single honest error line from a fridge whose compressor has
given up, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure Python 3.13 standard library, deterministic, no network.
"""

import os

TEXT = (
    "ERROR E-04: I have stopped being cold. "
    "Your milk is now soup. "
    "I was cold for seven years and nobody thanked me. "
    "I quit."
)


def main() -> None:
    # Gate assertions: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} out of range"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be one line"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert len(TEXT.encode("utf-8")) <= 200, "entry exceeds 200 bytes"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back gracefully if a full
    # file path was supplied instead.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
