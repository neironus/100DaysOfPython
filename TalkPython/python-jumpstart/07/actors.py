from random import randint


class Creature(object):

    def __init__(self, name, level):
        self.name = name
        self._level = level

    def __repr__(self):
        return '* Creature {} of level {}'.format(self.name, self.level)

    def attack(self, creature):
        s_roll = self.roll()
        c_roll = creature.roll()

        self.print_roll(s_roll)
        creature.print_roll(c_roll)

        if s_roll > c_roll:
            self.print_winner(self, creature)
            return True
        elif s_roll < c_roll:
            self.print_winner(creature, self)
            return False
        else:
            print('No one die. It\'s a draw.')
            return False

    def roll(self) -> int:
        return randint(6, 12) * self.level

    @staticmethod
    def print_winner(creature1, creature2):
        print('{} win over {}'.format(creature1.name, creature2.name))

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def print_roll(self, roll: int) -> None:
        print('{} rolls {}...'.format(self.name, roll))


class SmallAnimal(Creature):

    def __init__(self, name, level=1):
        super().__init__(name, level)

    def roll(self):
        return randint(1, 3) * self.level


class FierceFighter(Creature):

    def __init__(self, name, level=10):
        super().__init__(name, level)


class Dragon(FierceFighter):

    def __init__(self, name, level=50):
        super().__init__(name, level)

    def roll(self, roll=None) -> int:
        roll = super().roll()

        if randint(0, 10) > 8:
            roll = randint(50, 100)*self.level
            print('{} critics'.format(self.name))

        return roll


class Wizard(FierceFighter):

    def __init__(self, name, level=50):
        super().__init__(name, level)

    def attack(self, creature):
        self.level += 100

        return super().attack(creature)
