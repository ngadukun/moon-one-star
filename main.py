"""Print the entry line for the make.fun bounty "The Moon Gets One Star".

Reads line.txt, checks it is a single line within the 120-character cap,
and prints it unchanged.
"""

import sys
from pathlib import Path

MAX_CHARS = 120


def main() -> None:
    line = Path(__file__).with_name("line.txt").read_text(encoding="utf-8")
    line = line.rstrip("\n")
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars, cap is {MAX_CHARS}"
    print(line)
    sys.stderr.write(f"[{len(line)}/{MAX_CHARS} characters]\n")


if __name__ == "__main__":
    main()
