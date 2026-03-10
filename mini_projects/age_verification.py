from os import system
from time import sleep

while True:
    sleep(2)
    system("cls")
    age = input(f"Enter your age : ")
    try:
        age = int(age)
        if age <= 0:
            print(f"You are not born yet")
        elif age < 18:
            print(f"You are not adult, come back after {18-age} years.")
        elif age >= 18:
            print(f"Access Granted!")
    except ValueError:
        print(f"Invalid Input")