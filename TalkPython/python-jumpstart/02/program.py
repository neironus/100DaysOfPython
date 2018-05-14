from random import randint

min_number = 0
max_number = 100


def print_header() -> None:
    print('----------------------------------')
    print('       guess the number app')
    print('----------------------------------')


def ask_for_number() -> int:
    number = input('guess a number between {} and {} '.format(min_number, max_number))
    return int(number)


def main():
    print_header()
    result = randint(min_number, max_number)
    guess = -1

    msg_incorrect = 'Your guess of {} is {} than the number'

    while guess != result:
        guess = ask_for_number()
        if guess < result:
            print(msg_incorrect.format(guess, 'LOWER'))
        elif guess > result:
            print(msg_incorrect.format(guess, 'HIGHER'))
        else:
            print('Yes you\'ve got it. The number was {}'.format(result))


if __name__ == '__main__':
    main()