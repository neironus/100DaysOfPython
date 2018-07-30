from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User(object):
    def __init__(self, name):
        self.name = name
        self._transactions = []

    @property
    def karma(self):
        return sum(self.points)

    @property
    def fans(self):
        return len(self._transactions)

    @property
    def points(self):
        return [t.points for t in self._transactions]

    def __add__(self, other):
        self._transactions.append(other)
        self.points.append(other.points)

    def __repr__(self):
        return f'{self.name} has a karma of {self.karma} and {self.fans} fans'


if __name__ == '__main__':
    u = User('john')
    print(u.name)
