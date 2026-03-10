from os import system
from time import sleep

units = ["celsius", "farenhite", "kelvin"]


def title():
    title = f"===TEMPRATURE CONVERTER==="
    print(f"{title:^50}")


def menu():
    print(f"{'='*30}")
    print(f"1. Degree Celsius")
    print(f"2. Degree Farenhite")
    print(f"3. Kelvin")
    print(f"{'='*30}")


def celsius(value, unit):
    if unit == "celsius":
        c = value
    elif unit == "farenhite":
        c = (5 / 9) * (value - 32)
    elif unit == "kelvin":
        c = value - 273.15
    return c


def farenhite(value, unit):
    if unit == "farenhite":
        f = value
    elif unit == "celsius":
        f = ((9 / 5) * value) + 32
    elif unit == "kelvin":
        f = ((9 / 5) * (value - 273.15)) + 32
    return f


def kelvin(value, unit):
    if unit == "kelvin":
        k = value
    elif unit == "celsius":
        k = value + 273.15
    elif unit == "farenhite":
        k = (5 / 9) * (value - 32) + 273.15
    return k


while True:
    sleep(0.3)
    system("cls")
    title()
    menu()
    while True:
        unit = input(f"Choose a Unit (1,2 or 3) : ")
        try:
            unit = int(unit)
            if unit >= 1 and unit <= 3:
                unit = units[unit - 1]
                break
            else:
                print(f"The number must be from 1 to 3!")
        except ValueError:
            print(f"Invalid Input, please choose a number")
    while True:
        value = input(f"Enter the numerical value : ")
        try:
            value = float(value)
            break
        except ValueError:
            print(f"Invalid Input")
    c = f"{celsius(value, unit)}C"
    f = f"{farenhite(value, unit)}F"
    k = f"{kelvin(value, unit)}K"
    if unit == "celsius":
        print(f"FARENHITE : {f}")
        print(f"KELVIN : {k}")
    elif unit == "farenhite":
        print(f"CELSIUS : {c}")
        print(f"KELVIN : {k}")
    elif unit == "kelvin":
        print(f"CELSIUS : {c}")
        print(f"FARENHITE :{f}")
    
    q = input("Press Enter to continue or 'q' to quit...")
    if q.strip().lower() == 'q':
        break
