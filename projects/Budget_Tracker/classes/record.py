from datetime import datetime


class Record:
    def __init__(
        self,
        UID: int,
        title: str,
        amount: float,
        date: str,
        category: str,
        desc: str,
        timestamp,
    ):
        self.UID = UID
        self.title = title
        self.amount = amount
        self.timestamp = timestamp
        self.date = date
        self.category = category
        self.desc = desc
        

    @property
    def UID(self):
        return self._UID

    @UID.setter
    def UID(self, value):
        if isinstance(value, int) and value > 0:
            self._UID = value
        else:
            raise ValueError

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and value:
            self._title = value
        else:
            raise ValueError("'title' must be a string.")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, (int, float)) and value:
            self._amount = value
        else:
            raise ValueError("'amount' must a non-zero number")

    @property
    def amount_type(self):
        return "income" if self.amount > 0 else "expense"

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        try:
            datetime.strptime(value, "%d-%m-%Y")
            self._date = value
        except ValueError:
            self._date = self.timestamp[:10]

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and value:
            self._category = value
        else:
            self._category = "Uncategorized"

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        if isinstance(value, str):
            self._desc = value
        else:
            self._desc = ""

    def to_dict(self):
        record_dict = {
            "UID": self.UID,
            "title": self.title,
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "desc": self.desc,
            "timestamp": self.timestamp,
        }
        return record_dict

    @classmethod
    def to_record(cls, record_dict):
        record = cls(
            UID=record_dict["UID"],
            title=record_dict["title"],
            amount=record_dict["amount"],
            date=record_dict["date"],
            category=record_dict["category"],
            desc=record_dict["desc"],
            timestamp=record_dict["timestamp"],
        )
        return record

    def display(self, ledger):
        uuid_width = len(str(max([record.UID for record in ledger.ledger])))

        string = (
            f"================ TRANSACTION #{self.UID:<{uuid_width}} ================\n"
        )
        string += f"{'TITLE:':<13}{self.title}\n"
        string += f"{'DATE:':<13}{self.date}\n"
        string += f"{'AMOUNT:':<13}{abs(self.amount)}\n"
        string += f"{'TYPE:':<13}{self.amount_type.upper()}\n"
        string += f"{'CATEGORY:':<13}{self.category}\n"
        string += "---------------------------------------------------\n"
        if self.desc:
            string += f"DESCRIPTION:\n {self.wrap_text(self.desc, 9)}\n"
            string += f"===================================================\n"
        return string

    @staticmethod
    def wrap_text(string, wrap: int):
        string_list = string.split(" ")
        for i in range(wrap, len(string_list), wrap):
            string_list.insert(i, "\n")
        wrapped_string = " ".join(string_list)
        return wrapped_string
