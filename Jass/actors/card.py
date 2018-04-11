class Card(object):

    # Init
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    # Representation of card
    def __repr__(self):
        return 'Color {} - Rank {}'.format(self.color, self.rank)
