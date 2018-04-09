import itertools
import time
import random

def random_wait():
    return random.randint(3,7)

def main():
    colors = 'Red Orange Green Orange'.split()
    turn = itertools.cycle(colors)

    while True:
        change_color(next(turn))


def change_color(color):
    if (color == 'Orange'):
        print(color)
        time.sleep(1)
    elif (color == 'Red'):
        print('STOP!! The traffic light is {}'.format(color))
        time.sleep(random_wait())
    else:
        print('GO!! It\'s {}'.format(color))
        time.sleep(random_wait())

if __name__ == '__main__':
    main()
