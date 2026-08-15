# Handy cricket
import random

choices = ["batting", "balling"]
valid_options = [1, 2, 3, 4, 5, 6]


def get_comp_choice(plr_choice):
    if plr_choice == choices[1]:
        comp_choice = choices[0]
    else:
        comp_choice = choices[1]
    return comp_choice


def random_choice():
    return random.choice(choices)


def get_plr_choice():
    menu()
    while True:
        ch = input("Enter your choice (1-3): ")
        try:
            ch = int(ch)
            if 1<= ch <= 3:
                break
            else:
                print("Please choose the number between 1 and 3")
        except ValueError:
            print("The input must be integer")

    if ch == 1:
        plr_choice = choices[0]
    elif ch == 2:
        plr_choice = choices[1]
    elif ch == 3:
        plr_choice = random_choice()

    return plr_choice


def menu():
    print("*" * 10)
    print("1. Batting")
    print("2. Balling")
    print("3. Let Computer decide")
    print("*" * 10)


def batting(target: int = 0):
    print("\nIts Batting time!!!")
    runs = 0
    while True:
        while True:
            run = input("Enter the number of runs (1-6): ")
            try:
                run = int(run)
                if 1<=run <= 6:
                    break
                else:
                    print("The number must be between 1 to 6")
            except ValueError:
                print("the input must be integer")
        guess = random.choice(valid_options)
        print(f"Computer chose : {guess}")
        if run == guess:
            break
        else:
            runs += run
            print(f"Score : {runs}")
            if target != 0 and (target - runs) > 0:
                print(f"You only need {target - runs} runs to win the game!")

    return runs


def balling():
    runs = 0
    print("\nIts balling time!!!")
    while True:
        run = random.randint(1, 6)
        while True:
            plr_guess = input("Enter the number of runs (1-6) : ")
            try:
                plr_guess = int(plr_guess)
                if 1<= plr_guess <=6:
                    break
                else:
                    print("The number must be between 1 to 6")
            except ValueError:
                print("The input must be integer")

        print(f"Comp_scored {run} runs!")
        if run == plr_guess:
            break
        else:
            runs += run
            print(f"Total score of comp : {runs}")

    return runs


plr_choice = get_plr_choice()
comp_choice = get_comp_choice(plr_choice)

print(f"player_choice : {plr_choice} \ncomp_choice : {comp_choice}")


if plr_choice == choices[0]:
    plr_runs = batting(0)
    print(f"You scored {plr_runs} runs!")
    comp_runs = balling()
else:
    comp_runs = balling()
    print(f"Computer scored {comp_runs} runs!")
    plr_runs = batting(target=comp_runs + 1)
    print(f"You scored {plr_runs} runs!")

if plr_runs == comp_runs:
    print("The game is draw")
elif plr_runs > comp_runs:
    print(f"YOU WON THE GAME by {plr_runs - comp_runs} runs")
elif plr_runs < comp_runs:
    print(f"Oops, you lost the game by {comp_runs - plr_runs} runs, better luck next time.")