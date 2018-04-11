from actors.game import Game
from actors.player import Player


def main():
    p1 = Player('P1')
    p2 = Player('P2')
    p3 = Player('P3')
    p4 = Player('P4')

    game = Game([p1, p2, p3, p4])
    game.new_game()


if __name__ == '__main__':
    main()
