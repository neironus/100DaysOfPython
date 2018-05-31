from time import sleep

from actors import Wizard, Dragon, SmallAnimal, FierceFighter, Creature
from random import choice


def print_header():
    print('--------------------------')
    print('     Wizard Game app')
    print('--------------------------')


def ask_for_action() -> str:
    print()
    return input('What do you want to do ? [a]ttack [r]un or [l]ook around ')


def look_around(creatures: []) -> None:
    print('I see: ')
    for creature in creatures:
        print(creature)


def game_loop():
    creatures = [
        Creature(name='Tree', level=1),
        Dragon(name='Dragon'),
        FierceFighter(name='John'),
        SmallAnimal(name='Rat', level=3),
        SmallAnimal(name='Boar', level=5),
        Wizard(name='Evil Wizard', level=1000),
    ]

    hero = Wizard('Bob', level=75)

    while True:
        if not creatures:
            print_endgame()
            break

        creature = choice(creatures)

        print()
        print('A {} of level {} appear.'.format(creature.name, creature.level))

        action = ask_for_action()
        print()

        if action == 'a':
            if hero.attack(creature):
                creatures.remove(creature)
            else:
                print('I need more energy.')
                sleep(5)
                print('Ok I\'m back.')
        elif action == 'r':
            print('The wizard {} runs away!'.format(hero.name))
        elif action == 'l':
            look_around(creatures)
        else:
            print('OK leaving the game')
            break


def print_endgame():
    print()
    print('---------------------------------')
    print('All the monsters have been killed.')
    print('---------------------------------')
    print()


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
