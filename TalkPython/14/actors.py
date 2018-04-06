class Roll:
    def __repr__(self):
        print('{} - defeat: {} - defeated_by: {}'.format(self.name, self.defeat, self.defeated_by))

    def __init__(self, name, defeat, defeated_by):
        self.name = name
        self.defeat = defeat
        self.defeated_by = defeated_by

    def can_defeat(self, roll):
        return self.name in roll.defeated_by

class Player:
    def __repr__(self):
        print('{} - {} points'.format(self.name, self.points))

    def __init__(self, name):
        self.name = name
        self.points = 0

    def get_point(self):
        self.points += 1
