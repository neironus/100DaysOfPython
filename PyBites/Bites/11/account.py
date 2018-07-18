from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []
        self.toto = [1,2,3,4]

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def _validate_value(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError('Invalid error')

    def __len__(self):
        return len(self._transactions)

    # Using the total ordering decorator,
    # The class must define one of __lt__(), __le__(), __gt__(), or __ge__().
    # In addition, the class should supply an __eq__() method.
    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __getitem__(self, item):
        return self._transactions[item]

    # def __iter__(self):
    #     for t in self._transactions:
    #         yield t

    def __add__(self, other):
        self._validate_value(other)
        self._transactions.append(other)

    def __sub__(self, other):
        self._validate_value(other)
        self._transactions.append(-other)

    def __repr__(self):
        return '{} account - balance: {}'.format(self.name, self.balance)
