#!/usr/bin/env python3
"""Entry for 'The Funniest Toaster Error Message' (make.fun).

Writes the single-line toaster error message to /output/entry.txt.
The line is a deadpan appliance error: a jammed slice of bread that
has, bureaucratically, moved in for good.
"""

import os

LINE = "ERROR E7: Bread jammed in slot 2. It has filed for residency and won."


def main() -> None:
    # The gate allows 1-120 characters, one line, UTF-8. Fail loudly
    # here rather than shipping an entry the scorer would refuse.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
