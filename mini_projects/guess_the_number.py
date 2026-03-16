#IMPORTANT: You must have color.py, you can get it form my python-learning repo
import random
from os import system
from time import sleep
from color import Color

# variables
attempt = 0


def get_num(start, end):
    num = random.randint(start, end)
    return num


def title():
    title = f"{Color.bold}{Color.blue}===GUESS THE NUMBER!==={Color.reset}"
    print(f"{title:^100}")


def menu():
    print(f"{Color.green}{'='*34}{Color.reset}")
    print(f"{Color.bold}{Color.green}1. LEVEL-1 [EASY]   [1-100]")
    print(f"{Color.bold}{Color.yellow}2. LEVEL-2 [MEDIUM] [1-10000]")
    print(f"{Color.bold}{Color.red}3. LEVEL-3 [HARD]   [1-1000000]")
    print(f"{Color.bold}{Color.magenta}4. LEVEL-4 [EXTREME][1-100000000]")
    print(f"{Color.green}{'='*34}{Color.reset}")


def level():
    while True:
        level = input(f"{Color.bold}{Color.blue}LEVEL (1-4) : {Color.reset}")
        try:
            level = int(level)
            if level >= 1 and level <= 4:
                break
            else:
                print(f"{Color.red}The level must be from 1 to 4{Color.reset}")
        except ValueError:
            print(f"{Color.red}ERROR: Invalid Input{Color.reset}")
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
            guess = input(f"{Color.bold}{Color.blue}Enter your guess ({range}): {Color.reset}")
            try:
                guess = int(guess)
                break
            except ValueError:
                print(f"{Color.red}ERROR: Invalid Input{Color.reset}")
        if guess == number:
            print()
            print(
                f"{Color.bold}{Color.green}CONGRATUALTIONS!, the number was {number} and  you took {attempt} attempts{Color.reset}"
            )
            print()
            break
        elif guess < number:
            print(f"{Color.yellow}TOO LOW{Color.reset}")
            attempt += 1
        elif guess > number:
            print(f"{Color.yellow}TOO HIGH{Color.reset}")
            attempt += 1
    q = input(f"Press Enter to continue or 'q' to quit...")
    if q.strip().lower() == "q":
        break
