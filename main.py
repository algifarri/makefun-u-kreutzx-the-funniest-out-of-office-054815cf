#!/usr/bin/env python3
"""One-line out-of-office entry for make.fun's "The Funniest Out-of-Office".

Writes a single line, 140 characters at most, to /output/entry.txt:
an original out-of-office auto-reply with a deadpan twist — the
auto-reply itself is also out of office, so urgent mail is handed to
a stand-in that is equally unavailable. Deterministic, standard
library only, no input and no network.
"""

import os

ENTRY = (
    "I'm out of office until Monday. Urgent emails will be handled "
    "by my auto-reply, which is also out of office until Monday."
)


def main():
    # The gate allows 1-140 characters; the line is 121, and it is
    # written exactly, with no trailing newline, as one line. The
    # joke lands on the second sentence: the "help" on offer is a
    # second auto-reply that is out of office too.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
