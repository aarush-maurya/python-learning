from classes.account import Account
from classes.bank import Bank


def main():
    bank = Bank()
    acc1 = Account("Aarush", bank.create_acc_no())
    bank.add(acc1)
    acc2 = Account("David", bank.create_acc_no())
    bank.add(acc2)
    for acc in bank.accounts:
        print(f"Account Name: {acc.name} |  Account Number : {acc.acc_no}")


if __name__ == "__main__":
    main()
