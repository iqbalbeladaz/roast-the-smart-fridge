"""roast-the-smart-fridge: one line roasting the smart fridge.

The roast turns on the fridge as a judgmental roommate: it logs every
midnight snack, then greets the writer each morning with a salad recipe,
as if the appliance had seen everything and forgives nothing. The sting
lands in the last words, and the joke names two real smart-fridge
behaviours (inventory tracking and recipe suggestions) instead of the
stock gag about a fridge ordering too much milk.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = (
    "My smart fridge logs every midnight snack, then greets me each "
    "morning with a salad recipe \u2014 a roommate who saw everything "
    "and forgives nothing."
)

MAX_CHARS = 160


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
