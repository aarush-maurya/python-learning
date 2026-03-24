class Account:
    def __init__(self, name, acc_no) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("'name' must be a string")

    @property
    def acc_no(self):
        return self._acc_no

    @acc_no.setter
    def acc_no(self, value):
        if isinstance(value, str) and value.isdigit() and len(value) == 10:
            self._acc_no = value
        else:
            raise ValueError("'acc_no' must be a string and should of of 10 digits")

    def debit(self, value):
        if isinstance(value, (float, int)) and value <= self.balance:
            self.balance -= value
        else:
            raise ValueError(
                "'value' must be less or equal to the balance and should be a float or int"
            )

    def credit(self, value):
        if isinstance(value, (float, int)):
            self.balance += value
        else:
            raise ValueError("'value' must be a float or int")
