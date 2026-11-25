#!/usr/bin/env python3
"""Entry for make.fun bounty u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

Writes a ~100-word monologue for a fantasy villain who is secretly just
very tired to /output/entry.txt. The tiredness lives in the rhythm, the
pauses and the small deflections; he never announces it, and he is still
a villain with a scheme (he collects the dreams of kings) and a history
(nine years at these walls).
"""

import os

MONOLOGUE = (
    "Come closer, little king. No \u2014 sit. Standing hurts my knees, and I "
    "have stood at these walls nine years. Nine. I buried three armies, "
    "two prophets, one very loud herald. I recall every name but yours. "
    "It will come to me. It always does, near the third bell, when the "
    "dreams I stole start whispering. Yes, I collect the dreams of "
    "kings. Yours sit in a jar, somewhere. Forgive the dust. Forgive "
    "the pause. Even darkness blinks. Now kneel, and I will let you "
    "keep one dream. Pick the one where you were happy. Quickly \u2014 "
    "before I forget why I came."
)


def check_gate(text: str) -> None:
    """Fail loudly rather than write an entry the sealed scorer rejects."""
    chars = len(text)
    words = len(text.split())
    if not 1 <= chars <= 600:
        raise ValueError(f"entry is {chars} characters; gate allows 1-600")
    if not 90 <= words <= 110:
        raise ValueError(f"entry is {words} words; the brief asks for about 100")
    if not text.strip():
        raise ValueError("entry is only white space")


def main() -> None:
    check_gate(MONOLOGUE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(MONOLOGUE)


if __name__ == "__main__":
    main()
