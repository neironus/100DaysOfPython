from api import GameService


def print_header():
    print('GUESS NUMBER GAME')


def main():
    print_header()

    gs = GameService()

    try:
        id_game = gs.create_game().get('id')
        id_game = 'b28ee491-9cbe-4738-9e08-93ca9885dd7c'

        name = input('Name of player: ')
        user = gs.find_user(name=name)

        done = False

        while not done:
            guess = input('Your guess: ')

            guess_result = gs.make_a_guess(id_player=user.get('id'),
                                           id_game=id_game, guess=guess)

            status = guess_result.get('status')

            if status == 0:
                print('Your number is to low.')
            elif status == 2:
                print('Your number is too high.')
            else:
                print('Congratulation your guess the right number.')
                done = True

        print('BYE.')
    except Exception as e:
        print('> Error: {}'.format(
            e.response.text
        ))


if __name__ == '__main__':
    main()
