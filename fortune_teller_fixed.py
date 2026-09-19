# Fortune Teller (good version)
# Deb Samanta
# 9/18/26
# Same program as the other file but I actually used the stuff from lecture.
# DRY, single responsibility, and comments that aren't useless.

months = {
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
    "december": 12
}

love_fortunes = [
    "Someone you already know likes you more than you think.",
    "Don't text your ex this week.",
    "You will have a good conversation with a stranger.",
    "Stop overthinking it."
]

career_fortunes = [
    "Finish the assignment you keep putting off.",
    "A group project will actually be fine for once.",
    "Ask the question in class.",
    "Coffee will save you this week."
]

luck_fortunes = [
    "Your lucky color is blue.",
    "Look for a $5 on the ground.",
    "Skip the 3rd notification.",
    "If you find a penny keep it."
]


def get_name():
    """Asks for a name and keeps asking if they leave it blank."""
    name = input("What is your name? ").strip()
    while name == "":
        name = input("Please enter a name: ").strip()
    return name


def month_to_number(text):
    """Takes january or 3 or whatever and returns 1-12. Returns None if its not a month."""
    text = text.strip().lower()
    if text in months:
        return months[text]
    if text.isdigit():
        n = int(text)
        if n >= 1 and n <= 12:
            return n
    return None


def get_month():
    """Gets the birth month."""
    while True:
        ans = input("Birth month (name or 1-12): ")
        num = month_to_number(ans)
        if num != None:
            return num
        print("That's not a month, try again.")


def get_lucky_number():
    """Gets a lucky number. Has to be an int."""
    while True:
        ans = input("Lucky number: ")
        try:
            return int(ans)
        except ValueError:
            print("Please enter a number.")


def pick_fortune(fortunes, seed):
    # % so if you put the same month + lucky number you get the same fortune again
    return fortunes[seed % len(fortunes)]


def get_info():
    """Gets name, month, and lucky number. Doesn't pick fortunes."""
    print("====================")
    print(" FORTUNE TELLER")
    print("====================")
    name = get_name()
    month = get_month()
    lucky = get_lucky_number()
    return name, month, lucky


def make_fortunes(month, lucky):
    """Picks the 3 fortunes using the month and lucky number we already have."""
    seed = month + lucky
    love = pick_fortune(love_fortunes, seed)
    career = pick_fortune(career_fortunes, seed)
    luck = pick_fortune(luck_fortunes, seed)
    return love, career, luck


def print_fortunes(name, love, career, luck):
    """Just prints the reading, doesn't ask for anything."""
    print("------------------------------")
    print("Ok " + name + ", here's your reading")
    print("Love: " + love)
    print("Career: " + career)
    print("Luck: " + luck)
    print("------------------------------")
    print("bye " + name)


def main():
    name, month, lucky = get_info()
    love, career, luck = make_fortunes(month, lucky)
    print_fortunes(name, love, career, luck)


if __name__ == "__main__":
    main()
