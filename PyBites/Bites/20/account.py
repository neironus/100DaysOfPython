class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
    def __enter__(self):
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.balance < 0:
            self._transactions = self._copy_transactions


if __name__ == '__main__':
    account = Account()

    account + 10
    with account as acc:
        acc - 15

    print(account.balance)
    assert account.balance == 0
