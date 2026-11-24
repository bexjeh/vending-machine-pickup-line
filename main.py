"""Vending-machine pickup line entry.

Writes one pickup line, spoken by the vending machine itself to a
passing human, to MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt).

Deterministic: the same line, byte for byte, on every run. No network,
no model, no clock, no environment input.
"""

import os

# The line: the machine itself speaking, in its own world (buttons,
# sold-out light). Revised: tighter than the first draft -- "You pressed"
# for "You've pressed", "so ... just came on" for "and now ... is on",
# so the turn ("I'm taken") lands in the very last words.
LINE = "You pressed all my buttons, so my sold-out light just came on \u2014 I'm taken."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
