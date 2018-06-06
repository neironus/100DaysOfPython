import sqlite3
from contextlib import contextmanager
from typing import List

DB_NAME = 'inventory.db'


@contextmanager
def acces_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()


# Create the db if not found
def init_db() -> None:
    try:
        conn = sqlite3.connect(DB_NAME)
    except:
        print('Error init db')


def print_answer(message: str) -> None:
    print('> {}'.format(message))


# Remove non-alphanumeric chars
def scrub(name: str) -> str:
    return ''.join(c for c in name if c.isalnum())


def create_room(name: str) -> None:
    name = scrub(name)

    with acces_db() as cursor:
        cursor.execute('CREATE TABLE '+name+' (item text, cost real)')


def add_room() -> None:
    print('\r\n')
    name = input('Room name: ')
    create_room(name)
    print_answer('Room created')


# Get all the tables from sqlite
def list_rooms() -> List:
    rooms = []
    with acces_db() as cursor:
        cursor.execute('SELECT name from sqlite_master WHERE type="table"')

        for room in cursor:
            rooms.append(room[0])

    return rooms


def add_item(room: str) -> None:
    while True:
        name = input('Item name: ')
        cost = input('Item value: ')

        try:
            if name and cost:
                with acces_db() as cursor:
                    cursor.execute(
                        'INSERT INTO "{}" VALUES(?,?)'.format(room),
                        [name, float(cost)]
                    )

                print_answer('{} added'.format(name))

                choice = input('Hit Q to quit or any other key to add another '
                               'item: ')

                if choice.lower() == 'q':
                    break
                print('\r\n')
            else:
                print_answer('The name or the value can\'t be empty.')
        except ValueError:
            print_answer('The name or the cost are not valid value.')
        except Exception:
            print_answer('Unknown error append, please try again latter.')


def add_inventory() -> None:
    room = ask_for_room()

    add_item(room)


def ask_for_room() -> str:
    rooms = list_rooms()

    if not rooms:
        print_answer('No rooms')
        return

    while True:
        for room in rooms:
            print(room)

        print('\r\n')
        choice = input('Select a room: ')
        if choice in rooms:
            return choice
        else:
            print_answer('Room not valid')


def view_inventory() -> None:
    room = ask_for_room()

    print('\r\n')
    with acces_db() as cursor:
        cursor.execute('SELECT * FROM "{}"'.format(room))

        for item in cursor:
            print('{}: ${:.2f}'.format(item[0], item[1]))


def total_value() -> None:
    rooms = list_rooms()
    total = 0

    with acces_db() as cursor:
        for room in rooms:
            cursor.execute('SELECT * FROM "{}"'.format(room))
            for item in cursor:
                total += item[1]

    print_answer('Total value: ${:.2f}'.format(total))


def main_menu() -> None:
    while True:
        print('\r\n')
        menu = {
            '1': 'Add Room.',
            '2': 'Add Inventory.',
            '3': 'View Inventory List.',
            '4': 'Total Value.',
            '5': 'Exit.'
        }
        for key, value in sorted(menu.items()):
            print('{} {}'.format(key, value))
        print('\r\n')

        choice = input('Selection: ')
        
        if choice == '1':
            add_room()
        elif choice == '2':
            add_inventory()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            total_value()
        elif choice == '5':
            break
        else:
            print_answer('Invalid option')


def main() -> None:
    init_db()
    main_menu()


if __name__ == '__main__':
    main()
