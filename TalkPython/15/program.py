from actors import Roll, Player
import random, csv

def print_header():
    print('####################################')
    print('#### Rock - Paper - Scissor and 12 others possibilities GAME ###')
    print('#################################### \n')

def read_rolls():
    rolls = []
    with open('battle-table.csv', 'r') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            rolls.append(add_roll(row))

        return sorted(rolls, key = lambda x: x.name)

def add_roll(row):
    name = row['Attacker']
    del row['Attacker']
    del row[name]

    defeated_by = [x for x,y in row.items() if y == 'lose']
    return Roll(name, defeated_by)

def ask_for_roll(rolls):
    print('\n')
    print('Options :')
    for i,r in enumerate(rolls):
        print('{} for {}'.format(i, r.name))
    roll = input("Enter your choice \n")

    try:
        roll = int(roll)
    except ValueError:
        raise ValueError('Should be a number')

    if roll not in range(0, len(rolls)):
        raise ValueError('Value must be include between 0 and {}'.format(len(rolls)))

    return rolls[roll]

def get_players_name():
    return input("Enter your name ! \n")

def main():
    print_header()
    rolls = read_rolls()

    name = get_players_name()
    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = random.choice(rolls)

        try:
            p1_roll = ask_for_roll(rolls)
        except ValueError as ve:
            continue

        print("p1 roll: {} - p2 roll : {}".format(p1_roll.name, p2_roll.name))
        if(p1_roll == p2_roll):
            print('Same roll')
        else:
            text = "{} won. He have now {} points"
            if (p1_roll.can_defeat(p2_roll)):
                player1.add_point()
                print(text.format(player1.name, player1.points))
            else:
                player2.add_point()
                print(text.format(player2.name, player2.points))
        count += 1
    else:
        print('\n\n')
        text = "{} with {}points beats {} and his {}points"
        if (player1.points > player2.points):
            print(text.format(player1.name, player1.points, player2.name, player2.points))
        elif (player2.points > player1.points):
            print(text.format(player2.name, player2.points, player1.name, player1.points))
        else:
            print("It's a draw.")

if __name__ == '__main__':
    main()
