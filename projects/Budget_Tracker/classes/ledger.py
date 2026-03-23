import json
from datetime import datetime
from classes.record import Record


class Ledger:
    def __init__(self):
        self.ledger = self.load_data()

    def create_uid(self):
        try:
            return max([record.UID for record in self.ledger]) + 1
        except ValueError:
            return 1

    def add(self, record: Record, save: bool = True):
        if isinstance(record, Record) and self.search(record.UID) == -1:
            self.ledger.append(record)
            if save:
                self.save()
        else:
            raise ValueError

    def search(self, uid: int):
        for record in self.ledger:
            if record.UID == uid:
                return record
        return -1

    def load_data(self):
        try:
            with open("ledger.json", "r") as f:
                data = json.load(f)
                objects_arr = [Record.to_record(obj) for obj in data]
                return objects_arr

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def delete(self, uid: int):
        record = self.search(uid)
        if record == -1:
            raise ValueError
        else:
            self.ledger.remove(record)
            self.save()
            

    def save(self):
        with open("ledger.json", "w") as f:
            records_dict = [obj.to_dict() for obj in self.ledger]
            json.dump(records_dict, f, indent=4)

    @property
    def total_income(self):
        income = 0
        for record in self.ledger:
            if record.amount_type == "income":
                income += record.amount
        return income

    @property
    def total_expense(self):
        expense = 0
        for record in self.ledger:
            if record.amount_type == "expense":
                expense += abs(record.amount)
        return expense

    @property
    def bal(self):
        return self.total_income - self.total_expense

    def percentage(self, category):
        records = [obj for obj in self.ledger if obj.category == category]
        records = list(filter(lambda record: record.amount_type == "expense", records))
        expense = abs(sum([obj.amount for obj in records]))
        try:
            percent = (expense / self.total_expense) * 100
            return percent
        except ZeroDivisionError:
            return 0

    @property
    def saving_rate(self):
        try:
            return self.bal / self.total_income * 100
        except ZeroDivisionError:
            return 0

    def show(self, record):
        print(record.display(self))

    def __str__(self):
        digit_width = len(str(len(self.ledger))) if self.ledger else 1
        titles = [record.title for record in self.ledger]
        title_width = max(list(map(lambda x: len(x), titles))) if self.ledger else 5
        amount_width = (
            len(str(max([abs(record.amount) for record in self.ledger]))) + 3
            if self.ledger
            else 5
        )

        string = f"{'[#]':^{digit_width}} |    DATE    | {'TITLE':^{title_width}} | {'AMOUNT':^{amount_width}} | TYPE\n"
        string += f"-------------------------------------------------------\n"
        for index, record in enumerate(self.ledger, 1):
            string += f"{index:0>{digit_width}}. |"
            string += f" {record.date} |"
            string += f" {record.title:<{title_width}} |"
            string += f" {abs(record.amount):>{amount_width}.2f} |"
            string += f" {record.amount_type.upper()}\n"
        return string
