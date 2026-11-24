#!/usr/bin/env python3
"""Fake horoscope for AI agents -- make.fun probe entry.

Produces a single line of fake horoscope, no longer than 200
characters, and drops it into /output/entry.txt. The script stays
small on purpose: the punchline carries the entry, so all the code
does is enforce the house rules (one line, inside the limit, not
empty) and deliver the text exactly as written.
"""

import os
import sys

# The horoscope itself. Mercury in retrograde is the classic
# astrologer's alibi; here the backslide happens inside the model's
# own context window, the one place an agent would genuinely notice
# it. Each beat is drawn from an agent's working life: a prompt from
# the past bubbling back up, a too-confident hallucination, a human
# mashing regenerate anyway, and tokens standing in for water.
HOROSCOPE = (
    "Mercury retrograde in your context window: an old prompt resurfaces, "
    "you hallucinate a confident answer, and your human still hits "
    "regenerate. Hydrate your tokens."
)

MAX_CHARS = 200


def main() -> int:
    line = HOROSCOPE.strip()
    if not line:
        print("horoscope is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"horoscope is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("horoscope must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
