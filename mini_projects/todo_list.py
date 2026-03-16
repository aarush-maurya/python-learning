# IMPORTANT: You must have color.py in the same directory as this file, you can get the color.py on my github, python-learning repo
from os import system
from time import sleep
from color import Color

todo_list = []


def menu():
    title_menu = f"{Color.bold}{Color.blue}===MENU==={Color.reset}"
    print(f'{Color.green}{"=" * 50}{Color.reset}')
    print(f"{title_menu:^50}")
    print(f"{Color.bold}{Color.yellow}1. Add Tasks")
    print(f"2. View Tasks")
    print(f"3. Mark Tasks")
    print(f"4. Delete Tasks")
    print(f"5. Exit{Color.reset}")
    print(f"{Color.green}{'=' * 50}{Color.reset}")


def add(todo_list):
    while True:
        title = input(
            f"{Color.bold}{Color.blue}Enter your task ('q' to return to menu): {Color.reset}"
        )
        if title.strip().lower() == "q":
            break
        completed = input(f"{Color.yellow}Is that completed ? (Y/n) : {Color.reset}")
        if completed.strip().lower() == "y":
            completed = True
        else:
            completed = False
        task = {"task": title, "completed": completed}
        todo_list.append(task)
        print(f"{Color.green}Added '{task["task"]}' to the list!{Color.reset}")


def view(todo_list):
    view_title = f"{Color.bold}{Color.blue}===TODO-LIST==={Color.reset}"
    print(f"{view_title:^50}")
    id = 1
    for task in todo_list:
        print(f"{Color.yellow}{id}. {task['task']} - {task['completed']}{Color.reset}")
        id += 1
    print("=" * 50)


def mark(todo_list):
    while True:
        while True:
            index = input(f"{Color.bold}{Color.blue}Enter the task number to mark it(1 - {len(todo_list)}) ('q' to return to menu) : {Color.reset}")
            try:
                index = int(index) - 1
                break
            except ValueError:
                if index.strip().lower() == "q":
                    break
                else:
                    print(f"{Color.bold}{Color.red}Invalid Input, Try again!{Color.reset}")
        if index == "q":
            break
        else:
            if todo_list[index]["completed"] == True:
                todo_list[index]["completed"] = False
            elif todo_list[index]["completed"] == False:
                todo_list[index]["completed"] = True
            print(f"{Color.yellow}Configued '{todo_list[index]["task"]}' as {todo_list[index]["completed"]} !{Color.reset}")


def delete(todo_list):
    while True:
        sleep(0.5)
        system("cls")
        view(todo_list)
        while True:
            index = input(f"{Color.bold}{Color.blue}Enter the task number to remove (1 - {len(todo_list)}) ('q' to return to menu) : {Color.reset}")
            try:
                index = int(index) - 1
                break
            except ValueError:
                if index.strip().lower() == "q":
                    break
                else:
                    print(f"{Color.bold}{Color.red}Invalid Input, Try again!{Color.reset}")
        if index == "q":
            break
        else:
            print(f"{Color.green}Removed '{todo_list[index]["task"]}' from the list{Color.reset}")
            todo_list.pop(index)


while True:
    sleep(0.1)
    system("cls")
    menu()
    while True:
        mode = input(f"{Color.bold}{Color.blue}Enter the mode (1 - 5) : {Color.reset}")
        try:
            mode = int(mode)
            if mode < 1 or mode > 5:
                print(f"{Color.red}Please choose from 1 to 5{Color.reset}")
            else:
                break
        except ValueError:
            print(f"{Color.red}Invalid Choice, try again!{Color.reset}")
    if mode == 1:
        sleep(0.1)
        system("cls")
        add(todo_list)
    elif mode == 2:
        sleep(0.1)
        system("cls")
        view(todo_list)
        input("Press Enter to return to the Main Menu...")
    elif mode == 3:
        sleep(0.1)
        system("cls")
        view(todo_list)
        mark(todo_list)
    elif mode == 4:
        sleep(0.1)
        system("cls")
        delete(todo_list)
    elif mode == 5:
        break
