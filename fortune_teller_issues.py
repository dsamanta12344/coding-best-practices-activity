# Fortune Teller
# Deb Samanta
# 9/18/26
# this program tells your fortune based on your name and birthday
# I was gonna connect it to a website but I didnt have time

import random

n = ""
m = 0
num = 0
# leftover from when I thought I needed a database
url = "http://localhost:3000/fortunes"


def get_name():
    # this function gets the name
    global n
    print("====================")
    print(" FORTUNE TELLER")
    print("====================")
    # ask for name
    x = input("What is your name? ")
    # strip spaces
    x = x.strip()
    # if they hit enter with nothing
    if x == "":
        x = input("What is your name? ")
        x = x.strip()
        if x == "":
            x = "User"
    # print(x)
    # i = i + 1
    n = x
    # returns the age
    return x


def love_fortune():
    # love fortune
    global n
    global m
    global num
    print("----- love -----")
    month = input("Birth month (1-12 or name): ")
    month = month.strip().lower()
    if month == "1" or month == "january":
        m = 1
    elif month == "2" or month == "february":
        m = 2
    elif month == "3" or month == "march":
        m = 3
    elif month == "4" or month == "april":
        m = 4
    elif month == "5" or month == "may":
        m = 5
    elif month == "6" or month == "june":
        m = 6
    elif month == "7" or month == "july":
        m = 7
    elif month == "8" or month == "august":
        m = 8
    elif month == "9" or month == "september":
        m = 9
    elif month == "10" or month == "october":
        m = 10
    elif month == "11" or month == "november":
        m = 11
    elif month == "12" or month == "december":
        m = 12
    else:
        m = 1

    lucky = input("Lucky number: ")
    try:
        num = int(lucky)
    except:
        num = 7

    lines = []
    lines.append("Someone you already know likes you more than you think.")
    lines.append("Don't text your ex this week.")
    lines.append("You will have a good conversation with a stranger.")
    lines.append("Stop overthinking it.")
    i = (m + num) % 4
    # print the fortune
    print(n + ", love fortune:")
    print(lines[i])
    return lines[i]


def job_fortune():
    # career one (copied from love and changed the list)
    global n
    global m
    global num
    print("----- career -----")
    month = input("Birth month (1-12 or name): ")
    month = month.strip().lower()
    if month == "1" or month == "january":
        m = 1
    elif month == "2" or month == "february":
        m = 2
    elif month == "3" or month == "march":
        m = 3
    elif month == "4" or month == "april":
        m = 4
    elif month == "5" or month == "may":
        m = 5
    elif month == "6" or month == "june":
        m = 6
    elif month == "7" or month == "july":
        m = 7
    elif month == "8" or month == "august":
        m = 8
    elif month == "9" or month == "september":
        m = 9
    elif month == "10" or month == "october":
        m = 10
    elif month == "11" or month == "november":
        m = 11
    elif month == "12" or month == "december":
        m = 12
    else:
        m = 1

    lucky = input("Lucky number: ")
    try:
        num = int(lucky)
    except:
        num = 7

    lines = []
    lines.append("Finish the assignment you keep putting off.")
    lines.append("A group project will actually be fine for once.")
    lines.append("Ask the question in class.")
    lines.append("Coffee will save you this week.")
    i = (m + num) % 4
    print(n + ", career fortune:")
    print(lines[i])
    return lines[i]


def luck_fortune():
    # luck
    global n, m, num
    print("----- luck -----")
    month = input("what month were you born? ")
    month = month.strip().lower()
    if month == "1" or month == "january":
        m = 1
    elif month == "2" or month == "february":
        m = 2
    elif month == "3" or month == "march":
        m = 3
    elif month == "4" or month == "april":
        m = 4
    elif month == "5" or month == "may":
        m = 5
    elif month == "6" or month == "june":
        m = 6
    elif month == "7" or month == "july":
        m = 7
    elif month == "8" or month == "august":
        m = 8
    elif month == "9" or month == "september":
        m = 9
    elif month == "10" or month == "october":
        m = 10
    elif month == "11" or month == "november":
        m = 11
    elif month == "12" or month == "december":
        m = 12
    else:
        m = 1

    lucky = input("lucky number: ")
    try:
        num = int(lucky)
    except:
        num = 7

    lines = []
    lines.append("Your lucky color is blue.")
    lines.append("Look for a $5 on the ground.")
    lines.append("Skip the 3rd notification.")
    lines.append("If you find a penny keep it.")
    i = (m + num) % 4
    print(n + ", luck fortune:")
    print(lines[i])
    return lines[i]


def main():
    # runs everything
    get_name()
    love_fortune()
    job_fortune()
    luck_fortune()
    print("====================")
    print("bye " + n)
    print("====================")
    # TODO save to a file later
    # save(n, m, num)


main()
