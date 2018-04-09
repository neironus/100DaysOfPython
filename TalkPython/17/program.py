NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def reverse_first_last_name(name):
    first, last = name.split()
    return "{} {}".format(last, first)

def main():
    names_titles_cased = [name.title() for name in NAMES]
    print(names_titles_cased)

    names_last_name_first = [reverse_first_last_name(name) for name in NAMES]
    print(names_last_name_first)

if __name__ == '__main__':
    main()
