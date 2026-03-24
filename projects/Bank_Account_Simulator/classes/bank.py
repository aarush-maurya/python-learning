from classes.account import Account


class Bank:
    def __init__(
        self,
    ):
        self.accounts = []

    def add(self, account: Account):
        if isinstance(account, Account):
            self.accounts.append(account)

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        is_valid = True
        for account in accounts:
            if not isinstance(account, Account):
                is_valid = False
        if is_valid:
            self._accounts = accounts
        else:
            raise ValueError("'accounts' must contain instances of Account")

    def create_acc_no(self):
        try:
            max_acc_no = max(list(map(lambda x: int(x.acc_no), self.accounts)))
            return str(max_acc_no + 1)
        except ValueError:
            return "1000000000"
