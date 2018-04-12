from actors.card import Card

import random


class Round(object):

    # Init
    def __init__(self, roundNumber, players):
        self.roundNumber = roundNumber
        self.players = players

    # Create a new round
    def new_round(self):
        self.deal_players_cards(self._create_deck)

        if (self.roundNumber == 0):
            self._reorder_players_for_first_round()

    # Deal players cards
    def deal_players_cards(self, deck):
        deck = self._create_deck()

        for i, player in enumerate(self.players):
            player.hand = deck[i * 9:i * 9 + 9:]

    # Create a deck
    def _create_deck(self):
        deck = []
        colors = 'H D C S'.split()
        ranks = [6, 7, 8, 9, 10, 11, 12, 13, 14]

        for color in colors:
            for rank in ranks:
                deck.append(Card(color, rank))

        random.shuffle(deck)

        return deck

    def _turn_order(self):
        player = self.players.pop(0)
        self.players.append(player)

    # Reorder until players[0] have D7
    def _reorder_players_for_first_round(self):
        player = self.players[0]
        print(player.hand)

        if list(filter(
            lambda x: (x.color == 'D' and x.rank == 7), player.hand
        )):
            print(player.name, player.hand)
        else:
            self._turn_order()
            self._reorder_players_for_first_round()
