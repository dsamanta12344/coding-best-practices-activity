"""Command-line fortune booth.

Asks a visitor for a name, birth month, and lucky number, then prints one
short reading each for love, career, and luck. The same visitor answers are
reused for every category so the program does not re-ask the same questions.
"""

from __future__ import annotations

MONTH_NAMES = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

LOVE_LINES = (
    "Someone from your past will text at the worst possible time.",
    "A quiet kindness will matter more than a grand gesture.",
    "Stop rewriting the same argument in your head. Say it once.",
    "The right person will like the version of you that is not performing.",
)

CAREER_LINES = (
    "A small skill you keep skipping will unlock the next step.",
    "Say no to one extra task this week. Protect the work that matters.",
    "Ask the question you have been rehearsing in the hallway.",
    "Your next win comes from finishing, not from starting something new.",
)

LUCK_LINES = (
    "Carry a coin in your left pocket. You will need a yes-or-no later.",
    "Missed buses are trying to save you from a worse conversation.",
    "The lucky number is not magic. It is a reminder to pick a lane.",
    "Look up from your phone at 3:17. That is your cue.",
)


def prompt_nonempty(label: str) -> str:
    """Keep asking until the visitor types something other than whitespace."""
    while True:
        text = input(label).strip()
        if text:
            return text
        print("Please type a response.")


def parse_month(text: str) -> int | None:
    """Turn a month name or 1-12 into an integer month, or None if invalid."""
    cleaned = text.strip().lower()
    if cleaned in MONTH_NAMES:
        return MONTH_NAMES[cleaned]
    if cleaned.isdigit():
        value = int(cleaned)
        if 1 <= value <= 12:
            return value
    return None


def prompt_month() -> int:
    """Ask for a birth month until the visitor gives a usable value."""
    while True:
        parsed = parse_month(input("Birth month (1-12 or name): "))
        if parsed is not None:
            return parsed
        print("Please enter a month name or a number from 1 to 12.")


def prompt_lucky_number() -> int:
    """Ask for a whole number until the visitor gives one."""
    while True:
        raw = input("Lucky number: ").strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number, such as 7.")


def choose_line(lines: tuple[str, ...], seed: int) -> str:
    """Pick one line from a pool using a stable seed.

    The seed is built from the visitor's month and lucky number so the same
    person gets the same reading if they run the program twice.
    """
    return lines[seed % len(lines)]


def collect_visitor() -> tuple[str, int, int]:
    """Collect the three answers needed to build a reading."""
    print("==============================")
    print(" WELCOME TO THE FORTUNE BOOTH ")
    print("==============================")
    name = prompt_nonempty("What is your name? ")
    month = prompt_month()
    lucky_number = prompt_lucky_number()
    return name, month, lucky_number


def build_reading(month: int, lucky_number: int) -> dict[str, str]:
    """Choose one line for each category from the shared visitor answers."""
    seed = month + lucky_number
    return {
        "love": choose_line(LOVE_LINES, seed),
        "career": choose_line(CAREER_LINES, seed),
        "luck": choose_line(LUCK_LINES, seed),
    }


def print_reading(name: str, reading: dict[str, str]) -> None:
    """Display the finished reading. Does not collect input or pick lines."""
    sections = (
        ("Love reading", reading["love"]),
        ("Career reading", reading["career"]),
        ("Luck reading", reading["luck"]),
    )
    for title, line in sections:
        print("------------------------------")
        print(title)
        print("------------------------------")
        print(f"{name}, your {title.split()[0].lower()} fortune:")
        print(line)
    print("==============================")
    print(f"Goodbye {name}")
    print("==============================")


def main() -> None:
    name, month, lucky_number = collect_visitor()
    reading = build_reading(month, lucky_number)
    print_reading(name, reading)


if __name__ == "__main__":
    main()
