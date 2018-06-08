from game import Game
import game_service


def print_stats() -> None:
    stats = game_service.get_stats()
    if stats:
        print()
        print('-------------------------------')
        print('Regular players statistics')
        print('-------------------------------')
        print()
        for name, stat in stats.items():
            if sum(stat) > 0:
                print('{} with {} games avg of {:.2f} guesses.'.format(
                    name, len(stat), sum(stat)/len(stat)
                ))
        print()
        print()


def main() -> None:
    print_stats()
    name = input('What is your name? ')
    player = game_service.find_or_create_player(name)

    game = Game(player)
    game.game_loop()


if __name__ == '__main__':
    main()
