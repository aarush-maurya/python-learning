import random
import os
import time

options = {1: "Rock", 2: "Paper", 3: "Scissors"}


def choice():
    num = random.randint(1, 3)
    computer_choice = options[num]
    return computer_choice


def menu():
    print("=" * 50)
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("=" * 50)


def winner(computer_choice, player_choice):
    if computer_choice == player_choice:
        winner = "Draw"
    elif computer_choice == "Rock":
        if player_choice == "Paper":
            winner = "Player"
        else:
            winner = "Computer"
    elif computer_choice == "Paper":
        if player_choice == "Rock":
            winner = "Computer"
        else:
            winner = "Player"
    else:
        if player_choice == "Rock":
            winner = "Player"
        else:
            winner = "Computer"

    return winner


while True:
    time.sleep(0.1)
    os.system("cls")
    computer_choice = choice()
    menu()
    while True:
        player_choice = input(f"Enter you choice (1-3) : ")
        try:
            player_choice = int(player_choice)
            if player_choice > 0 and player_choice < 4:
                player_choice = options[player_choice]
                break
            else:
                print(f"Choice should be between 1 to 3!")
        except ValueError:
            print(f"Invalid Input, please enter Integer!")
    win = winner(computer_choice, player_choice)
    print(f"COMPUTER CHOICE : {computer_choice}\nPLAYER CHOICE : {player_choice}")
    if winner == "Draw":
        print("The game is draw!")
    elif winner == "Player":
        print("You WON!")
    else:
        print("Better luck next time :( ")

    q = input(f"Enter 'q' to quit or Enter to continue...")
    if q.strip().lower() == "q":
        break
