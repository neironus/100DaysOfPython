from actors.round import Round

import sys


class Game(object):

    # Init
    def __init__(self, players):
        self.rounds = []

        if (len(players) == 4):
            self.players = players
        else:
            print('They should be 4 players. Not more not less')
            sys.exit()

    # create a new game
    def new_game(self):
        self.new_round()

    # create a new round
    def new_round(self):
        rnd = Round(len(self.rounds), self.players)
        self.rounds.append(rnd)
        rnd.new_round()
