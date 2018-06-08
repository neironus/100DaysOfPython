import random
import uuid

import game_service

MAX_NUMBER = 100


class Game(object):

    def __init__(self, player):
        self.id = str(uuid.uuid4())
        self.player = player
        self.answer = random.randint(0, MAX_NUMBER)

        game_service.save_game(self.id, player.id, self.answer)

    def game_loop(self) -> None:
        guess_nb = 1
        while True:
            guess = self.ask_for_guess()
            print(guess)

            won = self.is_winning_guess(guess)

            game_service.save_guess(guess, guess_nb, won, self.id)

            if won:
                print('Congratulation you guess the right number '
                      '({}) with {}guesses'.format(guess, guess_nb))
                break
            else:
                if guess < self.answer:
                    print('Your guess is too low')
                else:
                    print('Your guess is above the answer')
                print()

            guess_nb += 1

    def ask_for_guess(self) -> int:
        guess = input('Choose a number between 0 and {}: '.format(MAX_NUMBER))

        try:
            guess = int(guess)

            if 0 <= guess <= MAX_NUMBER:
                return guess
            else:
                raise OutOfScopeException

        except ValueError:
            print('> Guess not valid')
            print()
            return self.ask_for_guess()
        except OutOfScopeException:
            print('> The guess is not include/equal between 0 and {}'.
                  format(MAX_NUMBER))
            print()
            return self.ask_for_guess()
        except:
            print('Unknown error, try again.')
            print()
            return self.ask_for_guess()

    def is_winning_guess(self, guess):
        return True if self.answer == guess else False


class OutOfScopeException(Exception):
    pass
