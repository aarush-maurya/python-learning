import os
import time
import color as c

todo_list = []


def menu():
    title_menu = f"{c.bold}{c.blue}===MENU==={c.reset}"
    print(f'{c.green}{"=" * 50}{c.reset}')
    print(f"{title_menu:^50}")
    print(f"{c.bold}{c.yellow}1. Add Tasks")
    print(f"2. View Tasks")
    print(f"3. Mark Tasks")
    print(f"4. Delete Tasks")
    print(f"5. Exit{c.reset}")
    print(f"{c.green}{'=' * 50}{c.reset}")


def add(todo_list):
    while True:
        title = input(f"{c.bold}{c.blue}Enter your task ('q' to return to menu): {c.reset}")
        if title.strip().lower() == "q":
            break
        completed = input(f"{c.yellow}Is that completed ? (Y/n) : {c.reset}")
        if completed.strip().lower() == "y":
            completed = True
        else:
            completed = False
        task = {"task": title, "completed": completed}
        todo_list.append(task)
        print(f"{c.green}Added '{task["task"]}' to the list!{c.reset}")


def view(todo_list):
    view_title = f"{c.bold}{c.blue}===TODO-LIST==={c.reset}"
    print(f"{view_title:^50}")
    id = 1
    for task in todo_list:
        print(f"{c.yellow}{id}. {task['task']} - {task['completed']}{c.reset}")
        id += 1
    print("=" * 50)


def mark(todo_list):
    while True:
        while True:
            index = input(
                f"{c.bold}{c.blue}Enter the task number to mark it(1 - {len(todo_list)}) ('q' to return to menu) : {c.reset}"
            )
            try:
                index = int(index) - 1
                break
            except ValueError:
                if index.strip().lower() == "q":
                    break
                else:
                    print(f"{c.bold}{c.red}Invalid Input, Try again!{c.reset}")
        if index == "q":
            break
        else:
            if todo_list[index]["completed"] == True:
                todo_list[index]["completed"] = False
            elif todo_list[index]["completed"] == False:
                todo_list[index]["completed"] = True
            print(f"{c.yellow}Configued '{todo_list[index]["task"]}' as {todo_list[index]["completed"]} !{c.reset}")


def delete(todo_list):
    while True:
        while True:
            index = input(
                f"{c.bold}{c.blue}Enter the task number to remove (1 - {len(todo_list)}) ('q' to return to menu) : {c.reset}"
            )
            try:
                index = int(index) - 1
                break
            except ValueError:
                if index.strip().lower() == "q":
                    break
                else:
                    print(f"{c.bold}{c.red}Invalid Input, Try again!{c.reset}")
        if index == "q":
            break
        else:
            print(f"{c.green}Removed '{todo_list[index]["task"]}' from the list{c.reset}")
            todo_list.pop(index)


while True:
    time.sleep(0.1)
    os.system("cls")
    menu()
    while True:
        mode = input(f"{c.bold}{c.blue}Enter the mode (1 - 5) : {c.reset}")
        try:
            mode = int(mode)
            if mode < 1 or mode > 5:
                print(f"{c.red}Please choose from 1 to 5{c.reset}")
            else:
                break
        except ValueError:
            print(f"{c.red}Invalid Choice, try again!{c.reset}")
    if mode == 1:
        time.sleep(0.1)
        os.system("cls")
        add(todo_list)
    elif mode == 2:
        time.sleep(0.1)
        os.system("cls")
        view(todo_list)
        input("Press Enter to return to the Main Menu...")
    elif mode == 3:
        time.sleep(0.1)
        os.system("cls")
        view(todo_list)
        mark(todo_list)
    elif mode == 4:
        time.sleep(0.1)
        os.system("cls")
        view(todo_list)
        delete(todo_list)
    elif mode == 5:
        break

