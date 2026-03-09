import random
from os import system
from time import sleep
import color as c

# variables
attempt = 0


def get_num(start, end):
    num = random.randint(start, end)
    return num


def title():
    title = f"{c.bold}{c.blue}===GUESS THE NUMBER!==={c.reset}"
    print(f"{title:^100}")


def menu():
    print(f"{c.green}{'='*34}{c.reset}")
    print(f"{c.bold}{c.green}1. LEVEL-1 [EASY]   [1-100]")
    print(f"{c.bold}{c.yellow}2. LEVEL-2 [MEDIUM] [1-10000]")
    print(f"{c.bold}{c.red}3. LEVEL-3 [HARD]   [1-1000000]")
    print(f"{c.bold}{c.magenta}4. LEVEL-4 [EXTREME][1-100000000]")
    print(f"{c.green}{'='*34}{c.reset}")


def level():
    while True:
        level = input(f"{c.bold}{c.blue}LEVEL (1-4) : {c.reset}")
        try:
            level = int(level)
            if level >= 1 and level <= 4:
                break
            else:
                print(f"{c.red}The level must be from 1 to 4{c.reset}")
        except ValueError:
            print(f"{c.red}ERROR: Invalid Input{c.reset}")
    return level


# main
while True:
    sleep(0.2)
    system("cls")
    title()
    menu()
    lvl = level()
    if lvl == 1:
        number = get_num(1, 100)
        range = "1-100"
    elif lvl == 2:
        number = get_num(1, 10000)
        range = "1-10000"
    elif lvl == 3:
        number = get_num(1, 1000000)
        range = "1-1000000"
    elif lvl == 4:
        number = get_num(1, 100000000)
        range = "1-100000000"

    while True:
        while True:
            guess = input(f"{c.bold}{c.blue}Enter your guess ({range}): {c.reset}")
            try:
                guess = int(guess)
                break
            except ValueError:
                print(f"{c.red}ERROR: Invalid Input{c.reset}")
        if guess == number:
            print()
            print(
                f"{c.bold}{c.green}CONGRATUALTIONS!, the number was {number} and  you took {attempt} attempts{c.reset}"
            )
            print()
            break
        elif guess < number:
            print(f"{c.yellow}TOO LOW{c.reset}")
            attempt += 1
        elif guess > number:
            print(f"{c.yellow}TOO HIGH{c.reset}")
            attempt += 1
    q = input(f"Press Enter to continue or 'q' to quit...")
    if q.strip().lower() == "q":
        break
