#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Prints the entry line and writes it to /output/entry.txt, which is
where this competition's harness reads the artifact.

The line was picked from twelve drafts duel-scored in candidates.md
against the kit's published judge criteria (scare that outlasts the
line, vivid concrete detail, originality, last word lands the blow).
Its horror is carried by two adjectives — "polished" and "warm" —
and by everything the sentence withholds about who holds the key.
"""

ENTRY = (
    "Someone keeps returning my spare key through the letterbox, "
    "polished clean, though I have never lent it to anyone; "
    "last night it came back warm."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, creating /output if needed."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def check_gate() -> None:
    """Fail loudly if the entry ever drifts outside the kit's gate:
    UTF-8 text of 1 to 200 characters, not only white space."""
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry is whitespace only"


def main() -> None:
    check_gate()
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
