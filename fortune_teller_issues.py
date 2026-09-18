# fortune teller program
# Author: me
# Last updated: 2019 (this date is wrong on purpose)
# This file creates fortunes for people who use the program.
# This file also gets input from the user.
# This file also prints stuff.
# This file also validates months.
# Changelog:
# - added fortunes
# - added more fortunes
# - removed database because we never needed a database
# - added print statements

import random

# global variables we will use everywhere
n = ""
m = 0
num = 0
# unused leftover from an old idea
database_url = "http://localhost:9999/fortunes"


def get_name():
    # this function gets the name
    global n
    print("==============================")
    print(" WELCOME TO THE FORTUNE BOOTH ")
    print("==============================")
    # ask for name
    x = input("What is your name? ")
    # strip spaces
    x = x.strip()
    # if empty, ask again
    if x == "":
        # empty string
        x = input("What is your name? ")
        x = x.strip()
        if x == "":
            x = "Friend"
    # add 1 to nothing (leftover debug)
    # i = i + 1
    # print("debug name=", x)
    n = x
    # returns the visitor's age
    return x


def love_fortune():
    # love fortune function that does love fortunes
    global n, m, num
    print("------------------------------")
    print("Love reading")
    print("------------------------------")
    # ask month again because we do not reuse the earlier value
    month_text = input("Birth month (1-12 or name): ")
    month_text = month_text.strip().lower()
    if month_text == "1" or month_text == "january":
        m = 1
    elif month_text == "2" or month_text == "february":
        m = 2
    elif month_text == "3" or month_text == "march":
        m = 3
    elif month_text == "4" or month_text == "april":
        m = 4
    elif month_text == "5" or month_text == "may":
        m = 5
    elif month_text == "6" or month_text == "june":
        m = 6
    elif month_text == "7" or month_text == "july":
        m = 7
    elif month_text == "8" or month_text == "august":
        m = 8
    elif month_text == "9" or month_text == "september":
        m = 9
    elif month_text == "10" or month_text == "october":
        m = 10
    elif month_text == "11" or month_text == "november":
        m = 11
    elif month_text == "12" or month_text == "december":
        m = 12
    else:
        # default month is 6 because that is my birthday
        m = 6

    lucky = input("Lucky number: ")
    try:
        num = int(lucky)
    except:
        num = 7

    # copy-pasted fortune picker
    lines = []
    lines.append("Someone from your past will text at the worst possible time.")
    lines.append("A quiet kindness will matter more than a grand gesture.")
    lines.append("Stop rewriting the same argument in your head. Say it once.")
    lines.append("The right person will like the version of you that is not performing.")
    # pick a random one using month and number for no documented reason
    idx = (m + num) % 4
    # print the fortune
    print(n + ", your love fortune:")
    print(lines[idx])
    # return unused value
    return lines[idx]


def job_fortune():
    # this is the job one, same as love but for jobs
    global n, m, num
    print("------------------------------")
    print("Career reading")
    print("------------------------------")
    month_text = input("Birth month (1-12 or name): ")
    month_text = month_text.strip().lower()
    if month_text == "1" or month_text == "january":
        m = 1
    elif month_text == "2" or month_text == "february":
        m = 2
    elif month_text == "3" or month_text == "march":
        m = 3
    elif month_text == "4" or month_text == "april":
        m = 4
    elif month_text == "5" or month_text == "may":
        m = 5
    elif month_text == "6" or month_text == "june":
        m = 6
    elif month_text == "7" or month_text == "july":
        m = 7
    elif month_text == "8" or month_text == "august":
        m = 8
    elif month_text == "9" or month_text == "september":
        m = 9
    elif month_text == "10" or month_text == "october":
        m = 10
    elif month_text == "11" or month_text == "november":
        m = 11
    elif month_text == "12" or month_text == "december":
        m = 12
    else:
        m = 6

    lucky = input("Lucky number: ")
    try:
        num = int(lucky)
    except:
        num = 7

    lines = []
    lines.append("A small skill you keep skipping will unlock the next step.")
    lines.append("Say no to one extra task this week. Protect the work that matters.")
    lines.append("Ask the question you have been rehearsing in the hallway.")
    lines.append("Your next win comes from finishing, not from starting something new.")
    idx = (m + num) % 4
    print(n + ", your career fortune:")
    print(lines[idx])
    return lines[idx]


def luck_fortune():
    # luck
    global n, m, num
    print("------------------------------")
    print("Luck reading")
    print("------------------------------")
    month_text = input("Birth month (1-12 or name): ")
    month_text = month_text.strip().lower()
    if month_text == "1" or month_text == "january":
        m = 1
    elif month_text == "2" or month_text == "february":
        m = 2
    elif month_text == "3" or month_text == "march":
        m = 3
    elif month_text == "4" or month_text == "april":
        m = 4
    elif month_text == "5" or month_text == "may":
        m = 5
    elif month_text == "6" or month_text == "june":
        m = 6
    elif month_text == "7" or month_text == "july":
        m = 7
    elif month_text == "8" or month_text == "august":
        m = 8
    elif month_text == "9" or month_text == "september":
        m = 9
    elif month_text == "10" or month_text == "october":
        m = 10
    elif month_text == "11" or month_text == "november":
        m = 11
    elif month_text == "12" or month_text == "december":
        m = 12
    else:
        m = 6

    lucky = input("Lucky number: ")
    try:
        num = int(lucky)
    except:
        num = 7

    lines = []
    lines.append("Carry a coin in your left pocket. You will need a yes-or-no later.")
    lines.append("Missed buses are trying to save you from a worse conversation.")
    lines.append("The lucky number is not magic. It is a reminder to pick a lane.")
    lines.append("Look up from your phone at 3:17. That is your cue.")
    idx = (m + num) % 4
    print(n + ", your luck fortune:")
    print(lines[idx])
    return lines[idx]


def do_everything():
    # MAIN FUNCTION that does everything the other functions did not
    get_name()
    # we call three almost identical functions
    love_fortune()
    job_fortune()
    luck_fortune()
    print("==============================")
    print("Goodbye " + n)
    print("==============================")
    # random leftover code that never runs
    # save_to_cloud(n, m, num)
    # send_email(n)


do_everything()
