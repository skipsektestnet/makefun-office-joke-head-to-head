"""Write the office joke to /output/entry.txt."""

import os

ENTRY_TEXT = "Our thirty-minute standup ran so long that by the end, two people had been promoted and one had retired."
MAX_CHARS = 200


def validate(text):
    assert text.strip(), "entry text must not be empty"
    assert 1 <= len(text) <= MAX_CHARS, "entry text must be 1-200 characters"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert "  " not in text, "entry must not contain double spaces"


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} characters, {len(ENTRY_TEXT.split())} words")


if __name__ == "__main__":
    main()
