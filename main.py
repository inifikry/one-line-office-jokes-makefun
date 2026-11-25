"""One-Line Office Jokes — make.fun entry.

Writes a single line of office humour to /output/entry.txt.
Deterministic: the same line on every run, no network, no input.
"""

import os

JOKE = "I put 'per my last email' in my out-of-office reply, so the argument continues without me."


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "joke must be 1..200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
