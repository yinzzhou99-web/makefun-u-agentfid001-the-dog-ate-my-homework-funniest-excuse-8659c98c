"""Dog excuse entry: a one-line excuse, written to /output/entry.txt."""

from pathlib import Path

LINE = "You left it on the floor. The floor is where food goes. I followed the rules and now you're mad at me?"
# The dog's defence rests on one household law: food on the floor is fair game.

TARGET = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
