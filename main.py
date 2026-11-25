"""Passive-aggressive fridge note: read the note, put it on the door."""

import os


def load_note(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    note = load_note(os.path.join(os.path.dirname(__file__), "entry.txt"))
    if not note or len(note) > 200:
        raise ValueError("fridge note must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(note)
    print(note)


if __name__ == "__main__":
    main()
