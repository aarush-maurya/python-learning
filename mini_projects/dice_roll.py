import random


def rollDice():
    num = random.randint(1, 6)
    return num


while True:
    roll_amount = input(f"Enter the number of times to roll the dice :")
    try:
        roll_amount = int(roll_amount)
        if roll_amount > 0:
            break
        else:
            print("The number has to be greater than 0")
    except ValueError:
        print(f"Invalid input, try again!")

no_1 = 0
no_2 = 0
no_3 = 0
no_4 = 0
no_5 = 0
no_6 = 0
times_rolled = 0

while times_rolled < roll_amount:

    num = rollDice()
    if num == 1:
        no_1 += 1
    elif num == 2:
        no_2 += 1
    elif num == 3:
        no_3 += 1
    elif num == 4:
        no_4 += 1
    elif num == 5:
        no_5 += 1
    elif num == 6:
        no_6 += 1

    print(f"{times_rolled + 1}. {num}")
    times_rolled += 1

print(f"Number of times '1' occured : {no_1:^3}, percentage : {round((no_1/roll_amount * 100), 2)}")
print(f"Number of times '2' occured : {no_2:^3}, percentage : {round((no_2/roll_amount * 100),2)}")
print(f"Number of times '3' occured : {no_3:^3}, percentage : {round((no_3/roll_amount * 100),2)}")
print(f"Number of times '4' occured : {no_4:^3}, percentage : {round((no_4/roll_amount * 100),2)}")
print(f"Number of times '5' occured : {no_5:^3}, percentage : {round((no_5/roll_amount * 100),2)}")
print(f"Number of times '6' occured : {no_6:^3}, percentage : {round((no_6/roll_amount * 100),2)}")

input("Hit Enter to Exit...")