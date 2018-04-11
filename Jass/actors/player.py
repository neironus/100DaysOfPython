class Player(object):

    # Init
    def __init__(self, name):
        self._name = name
        self._hand = []

    #name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    #hand
    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand
