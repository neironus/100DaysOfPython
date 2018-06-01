import os
from collections import namedtuple

tupleFindText = namedtuple('TupleFindText', 'file idx text')


def print_header():
    print('------------------------------')
    print('   File search app')
    print('------------------------------')


def ask_for_directory() -> str:
    directory = input('What directory do you want to search: ')

    if not directory:
        return None

    full_path = os.path.abspath(directory)

    if not os.path.isdir(full_path):
        return None

    return full_path


def list_file_in_directory(directory: str) -> None:
    # directory = os.path(directory)
    # print(directory)
    if os.path.isdir(directory):
        for f in os.listdir(directory):
            print(f)


def ask_for_text_search() -> str:
    return input('What string are you looking for: ')


def get_files_in_directory(directory: str, recursive: bool = True):
    if os.path.basename(directory).startswith('.'):
        return

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if recursive and os.path.isdir(full_path):
            yield from get_files_in_directory(full_path, recursive)
        else:
            yield full_path


def search_text_in_files(files, text: str):
    for file in files:
        try:
            with open(file, 'r') as f:
                for idx, line in enumerate(f.readlines()):
                    if line.lower().find(text) >= 0:
                        custom_path = file.split('/')[4::]
                        yield tupleFindText("/".join(custom_path), idx,
                                            line.strip())
        except UnicodeDecodeError:
            pass
        except Exception as e:
            print('Error {} with file {}'.format(e, file))


def main():
    print_header()

    directory = ask_for_directory()
    if not directory:
        print('Invalid directory')
        return

    text = ask_for_text_search()
    if not text:
        print('We can\'t search for nothing')
        return

    files = get_files_in_directory(directory)
    founds = search_text_in_files(files, text)

    print_founds(founds)

    print('End Search.')


def print_founds(founds):
    print()
    print()
    i = 0
    for f in founds:
        i += 1
        print('{}, line {}>> {}'.format(f.file, f.idx, f.text))
    if i:
        print('{} total matches'.format(i))

    print()


if __name__ == '__main__':
    main()
