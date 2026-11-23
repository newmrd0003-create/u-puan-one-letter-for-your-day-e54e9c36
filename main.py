#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one character, the letter J, to entry.txt.
J stands for "jinxed": a day where everything that could go wrong did,
as if cursed.

Stdlib only, no network. Output is a single byte, no trailing newline.
"""

import os

LETTER = "J"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Guard + read-back verify: the gate requires exactly one A-Z character.
    with open(path, "rb") as f:
        raw = f.read()
    assert len(raw) == 1, f"entry must be exactly 1 byte, got {len(raw)}"
    text = raw.decode("utf-8")
    assert len(text) == 1 and "A" <= text <= "Z", f"entry must be one A-Z letter, got {text!r}"


if __name__ == "__main__":
    main()
