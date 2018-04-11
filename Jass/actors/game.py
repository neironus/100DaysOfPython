from actors.round import Round


class Game(object):

    # Init
    def __init__(self, players):
        self.rounds = []

        if (len(players) == 4):
            self.players = players
        else:
            return 'The numbers of players is incorrect'

    # create a new game
    def new_game(self):
        self.new_round()

    def new_round(self):
        rnd = Round(self.players)
        self.rounds.append(rnd)
        rnd.new_round()
