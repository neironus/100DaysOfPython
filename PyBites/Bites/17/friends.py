import itertools

def friends_teams(friends, team_size = 2, order_does_matter = False):
    if order_does_matter:
        return itertools.permutations(friends, team_size)
    else:
        return itertools.combinations(friends, team_size)


def main():
    friends = 'Bob Dante Julian Martin'.split()
    t = list(friends_teams(friends))
    print(t)

if __name__ == '__main__':
    main()
