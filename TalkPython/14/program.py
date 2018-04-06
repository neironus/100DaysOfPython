from actors import Roll, Player
import random

rolls = []

def print_header():
    print('#### Rock - Paper - Scissor Game ### \n')

def build_the_three_rolls():
    rock = rolls.append(Roll('rock', 'scissor', 'paper'))
    paper = rolls.append(Roll('paper', 'rock', 'scissor'))
    scissor = rolls.append(Roll('scissor', 'paper', 'rock'))

def ask_for_roll():
    print('\n')
    roll = input("What do you want to roll ? Enter 0 for rock, 1 for paper and 2 for scissor \n")

    try:
        roll = int(roll)
        if (0 <= roll <= 2):
            return rolls[roll]
        else:
            print('> Invalid choice')
            return ask_for_roll()

    except Exception as e:
        print('> Invalid choice')
        return ask_for_roll()

def get_players_name():
    return input("Enter your name ! \n")

def main():
    print_header()

    build_the_three_rolls()

    name = get_players_name()
    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2)

def game_loop(player1, player2):
    count = 1
    while count < 10:
        p2_roll = random.choice(rolls)
        p1_roll = ask_for_roll()

        print("p1 roll: {} - p2 roll : {}".format(p1_roll.name, p2_roll.name))
        if(p1_roll == p2_roll):
            print('Same roll')
        else:
            if (p1_roll.can_defeat(p2_roll)):
                player1.get_point()
                print("{} won. He have now {} points".format(player1.name, player1.points))
            else:
                player2.get_point()
                print("{} won. He have now {} points".format(player2.name, player2.points))
        count += 1
    else:
        print('\n\n')
        if (player1.points > player2.points):
            print("{} with {}points beats {} and his {}points".format(player1.name, player1.points, player2.name, player2.points))
        elif (player2.points > player1.points):
            print("{} with {}points beats {} and his {}points".format(player2.name, player2.points, player1.name, player1.points))
        else:
            print("It's a draw.")

if __name__ == '__main__':
    main()
