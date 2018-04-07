class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_point(self):
        self.points += 1

class Roll:
    def __str__(self):
        return self.name

    def __init__(self, name, defeated_by):
        self.name = name
        self.defeated_by = sorted(defeated_by)

    def can_defeat(self, roll):
        return self.name in roll.defeated_by
