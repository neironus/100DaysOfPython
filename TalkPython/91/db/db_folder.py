import os


def get_db_path(base_file):
    dir_path = os.path.dirname(__file__)
    return os.path.join(dir_path, base_file)
