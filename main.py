"""One-liner comedy joke generator.

Writes a single original one-line joke to /output/entry.txt.
Deterministic: it always writes the same joke.

The joke redefines "work-life balance" as panicking about both at
once -- the setup promises a wellness win, the punchline delivers
the opposite, in one deadpan breath.
"""

import os

JOKE = "I finally achieved work-life balance: I now panic about work and life at exactly the same time."

OUT_DIR = "/output"


def main() -> None:
    # The entry must be one line, 1-280 characters, not blank.
    assert 1 <= len(JOKE) <= 280
    assert "\n" not in JOKE and JOKE.strip() == JOKE
    os.makedirs(OUT_DIR, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
