# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def isValidWalk(walk):
    map = {'n': 0, 's': 0, 'w': 0, 'e':0}

    if len(walk) > 1 and len(walk) <= 10:
        for w in walk:
            map[w] += 1

        return map['n'] == map['s'] and map['w'] == map['e']

    else:
        return False
