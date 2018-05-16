import os
from collections import namedtuple
from typing import List

import pyperclip
import csv

clipboard = namedtuple('Clipboard', 'title, content')


def paste_from_clipboard() -> str:
    return pyperclip.paste()


def copy_to_clipboard(text: str) -> None:
    pyperclip.copy(text)


def load_saved_clipboard(file_path: str) -> List[clipboard]:

    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        return [clipboard(**row) for row in reader]


def save_saved_clipboard(file_path: str, saved_clipboard: List[clipboard]) \
        -> None:
    with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(clipboard._fields)
        writer.writerows(
            [[c.title, c.content] for c in saved_clipboard]
        )


def get_file_path() -> str:
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, 'datas')

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)

    file_path = os.path.join(full_path, 'saved.csv')

    return file_path


def valid_index(idx, saved_clipboard):
    return 0 <= idx < len(saved_clipboard)


def run_loop(saved_clipboard: List[clipboard]) -> List[clipboard]:
    c = -1

    while c != 'q':
        c = input('\nWhat do you want do to ? [a]dd, [g]et, [l]ist, [r]emove '
                  '[q]uit \n')
        
        if c == 'a':
            add_to_list(saved_clipboard)
        elif c == 'g':
            cl = get_from_list(saved_clipboard)
            copy_to_clipboard(cl.content)
            print('> Copy to clipboard')
        elif c == 'l':
            list_saved_clipboard(saved_clipboard)
        elif c == 'r':
            remove_from_list(saved_clipboard)
        elif c != 'q':
            print('> Invalid choice')

    return saved_clipboard


def remove_from_list(saved_clipboard: List[clipboard]):
    idx = int(input('Index :'))
    if valid_index(idx, saved_clipboard):
        del saved_clipboard[idx]
        print('Index deleted')


def list_saved_clipboard(saved_clipboard: List[clipboard]):
    for idx, cl in enumerate(saved_clipboard):
        print('[{}] - {}'.format(idx, cl.title))


def get_from_list(saved_clipboard: List[clipboard]) -> clipboard:
    try:
        idx = int(input('Index: '))
        if valid_index(idx, saved_clipboard):
            return saved_clipboard[idx]
    except Exception:
        print('> Invalid choice')


def add_to_list(saved_clipboard) -> None:
    title = input('Title: ')
    cl = clipboard(title, paste_from_clipboard())
    saved_clipboard.append(cl)
    print('> {} - {} added'.format(cl.title, cl.content))


def main():
    file_path = get_file_path()
    saved_clipboard = load_saved_clipboard(file_path)

    saved_clipboard = run_loop(saved_clipboard)

    save_saved_clipboard(file_path, saved_clipboard)


if __name__ == '__main__':
    main()
