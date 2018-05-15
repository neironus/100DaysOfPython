import platform
import shutil
import subprocess
import os
from typing import IO

import requests

def print_headers():
    print('-------------------------------')
    print('        Cat factory app')
    print('-------------------------------')


def get_path_save() -> str:
    base_folder = os.path.dirname(__file__)
    imgs_folder = 'imgs'
    full_path = os.path.join(base_folder, imgs_folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)

    return full_path


def get_lolcat() -> IO:
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    res = requests.get(url, stream=True)
    return res.raw


def write_file(path: str, cat: IO, filename: str) -> None:
    filename = os.path.join(path, filename + '.jpg')
    with open('{}'.format(filename), 'wb') as file:
        shutil.copyfileobj(cat, file)


def open_explorer(folder: str):
    if platform.system() == 'Linux':  # Linux
        subprocess.call(['xdg-open', folder])
    elif platform.system() == 'Windows':  # Windows
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Darwin':  # Mac
        subprocess.call(['open', folder])
    else:
        print('Unknown platform {}'.format(platform.system()))


def main():
    print_headers()

    full_path = get_path_save()

    for x in range(1, 11):
        cat = get_lolcat()
        print('Downloading lolcat-{}'.format(x))
        write_file(path=full_path, cat=cat, filename='lolcat-{}'.format(x))


    open_explorer(full_path)


if __name__ == '__main__':
    main()
