from os import system
from time import sleep

symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def title():
    title = f"===ROMAN TO INTEGER==="
    print(f"{title:^50}")


while True:
    sleep(0.3)
    system("cls")
    title()
    roman = input(f"Enter the roman number : ")
    roman = roman.strip().upper()
    rev_roman = roman[::-1]
    number = symbols[rev_roman[0]]
    i = 0
    while i < len(rev_roman):
        try:
            if symbols[rev_roman[i]] > symbols[rev_roman[i + 1]]:
                number -= symbols[rev_roman[i + 1]]
            else:
                number += symbols[rev_roman[i + 1]]
        except IndexError:
            pass
        i += 1
    print(f"\nROMAN : {roman}\nNUMBER : {number}\n")

    q = input(f"Press Enter to continue or 'q' to quit...")
    if q.strip().lower() == 'q':
        break
