from actors.card import Card

import random


class Round(object):

    # Init
    def __init__(self, roundNumber, players):
        self.roundNumber = roundNumber
        self.players = itertools.cycle(players)

    # Create a new round
    def new_round(self):
        self.deal_players_cards(self._create_deck)

    # Deal players cards
    def deal_players_cards(self, deck):
        deck = self._create_deck()

        for i, player in enumerate(self.players):
            player.hand = deck[i * 9:i * 9 + 9:]

    # Create a deck
    def _create_deck(self):
        deck = []
        colors = 'H D C S'.split()
        ranks = '6 7 8 9 10 J Q K A'.split()

        for color in colors:
            for rank in ranks:
                deck.append(Card(color, rank))

        random.shuffle(deck)

        return deck
