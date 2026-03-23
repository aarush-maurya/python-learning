import os
from time import sleep

from classes.ledger import Ledger
from classes.record import Record
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    string = "========== MENU ============\n"
    string += f"[1] Add Transaction\n"
    string += f"[2] View All (Tabular)\n"
    string += f"[3] Detailed Inspection\n"
    string += f"[4] Financial Analytics\n"
    string += f"[5] Delete Entry\n"
    string += f"[6] Exit\n"
    return string


def get_record(ledger: Ledger, quit=False):
    if not quit:
        number = input("Enter the record # :")
    else:
        number = input("Enter the record # or press 'q' to goto main menu:")
    try:
        if quit:
            if number.strip().lower() == "q":
                return "q"
        number = int(number)
        if 0 < number <= len(ledger.ledger):
            return number - 1

    except ValueError:
        raise ValueError("Invalid #")


def main():
    clear_screen()
    ledger = Ledger()
    print(menu())
    choice = input("Enter your choice : ")
    if choice == "1":
        try:
            uid = ledger.create_uid()
            title = input(f"Enter the title: ")
            amount = float(input(f"Enter the amount: "))
            is_income = input(f"Is this is an Income? (y/N):")
            if is_income.lower() == "y":
                pass
            else:
                amount = -amount
            date = input(
                f"Enter the date (DD-MM-YYYY) or press 'Enter' for current time: "
            )
            category = input(f"Enter the category or press 'Enter' for uncategorized: ")
            desc = input(f"Enter the description: ")
            timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            record = Record(
                UID=uid,
                title=title,
                amount=amount,
                date=date,
                category=category,
                desc=desc,
                timestamp=timestamp,
            )
            ledger.add(record)
            print("Record added Successfully!")
        except ValueError as e:
            print(f"ERROR: {e}")
        finally:
            sleep(1)

    elif choice == "2":
        if not ledger.ledger:
            print("The ledger is empty.")
            sleep(1)
        else:
            clear_screen()
            print(ledger)
            input(f"Press Enter to go back...")

    elif choice == "3":
        if not ledger.ledger:
            print("The ledger is empty.")
            sleep(1)
        else:
            try:
                while True:
                    clear_screen()
                    print(ledger)
                    print()
                    num = get_record(ledger, quit=True)
                    if num == "q":
                        break
                    clear_screen()
                    ledger.show(ledger.ledger[num])
                    input(f"Press Enter to go back...")

            except ValueError as e:
                print(f"ERROR: {e}")
                sleep(2)

    elif choice == "4":
        clear_screen()
        string = f"TOTAL INCOME: {ledger.total_income:.2f} INR\n"
        string += f"TOTAL EXPENSES: {ledger.total_expense:.2f} INR\n"
        string += f"------------------------------\n"
        string += f"CURRENT BALANCE: {ledger.bal:.2f} INR\n"
        string += f"SAVINGS RATE: {ledger.saving_rate:.2f}%\n"
        print(string)
        input(f"Press Enter to go back...")

    elif choice == "5":
        if not ledger.ledger:
            print("The ledger is empty.")
            sleep(1)
        else:
            clear_screen()
            print(ledger)
            try:
                num = get_record(ledger)
                uid = ledger.ledger[num].UID
                confirm = input(
                    f"Are you sure to delete Transaction #{uid}? (y/N): "
                )
                if confirm.lower() == "y":
                    ledger.delete(uid)
                    print(
                        f"Record with transaction ID #{uid} is deleted successfully."
                    )
                    sleep(2)
            except ValueError as e:
                print(f"ERROR: {e}")
                sleep(2)

    elif choice == "6":
        return "q"

    else:
        print(f"'Invalid Choice.")


if __name__ == "__main__":
    while True:
        q = main()
        if q == "q":
            exit()
