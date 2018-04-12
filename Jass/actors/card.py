class Card(object):

    # Init
    def __init__(self, color, rank):
        self._color = color
        self._rank = rank

    # String of card
    def __str__(self):
        return 'Color {} - Rank {}'.format(self.color, self.symbol)

    # color GET
    @property
    def color(self):
        return self._color

    # rank GET
    @property
    def rank(self):
        return self._rank

    # symbol GET
    @property
    def symbol(self):
        if self.rank == 14:
            return 'A'
        elif self.rank == 13:
            return 'K'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 11:
            return 'J'
        else:
            return self.rank
