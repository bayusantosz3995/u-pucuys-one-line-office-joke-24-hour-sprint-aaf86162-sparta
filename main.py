#!/usr/bin/env python3
"""One-line office joke entry for make.fun's "One-Line Office Joke: 24-Hour Sprint".

The joke: the polite corporate "per my last email" — the third reply to the
same thread, same attachment, sent at 09:14 — escalating from re-sending the
attachment to re-sending the calendar invite to re-sending a resignation.
Setup is the email thread every office worker recognises (the answer was on
page 2 all along); the punchline lands on the last three words, in that
order, and nothing is explained after it.
"""

import os
import sys

TEXT = (
    "Per my last email (09:14, third reply, same attachment): the answer is "
    "on page 2. I have now re-sent the attachment, the invite, and my "
    "resignation \u2014 in that order."
)


def main() -> int:
    text = TEXT
    # Gate: one line, 1-200 characters, not only whitespace.
    if not text or not text.strip():
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"gate failed: {len(text)} chars > 200", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
