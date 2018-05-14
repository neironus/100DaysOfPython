import sys
from typing import List, Any

from journal import Journal

j = Journal(name='journal')


def print_headers() -> None:
    print('------------------------')
    print('       JOURNAL APP')
    print('------------------------')


def run_event_loop() -> None:
    action = ''
    while action != 'x':
        print('\nWhat do you want to do ? ')
        action = input('[l]ist the entries. [a]dd a entry. e[x]it ')
        action = action.lower().strip()

        if action == 'l':
            j.list_entry()
        elif action == 'a':
            text = input('Add entry: ')
            j.add_entry(text)
        elif action != 'x':
            print('> Invalid option')


def exit_headers():
    print('Bye :\'(')


def main():
    print_headers()
    run_event_loop()
    j.save_journal()
    exit_headers()


if __name__ == '__main__':
    main()
