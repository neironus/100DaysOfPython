import os


class Journal(object):

    def __init__(self, name: str):
        """
        Journal
        :param name: journal name
        """
        self.filename = os.path.abspath(os.path.join('.', 'datas', name+'.txt'))
        self.entries = self.read_journal()

    def read_journal(self) -> list:
        if os.path.exists(self.filename):
            with open(self.filename) as file:
                return [line.strip('\n') for line in file.readlines()]
        else:
            return []

    def save_journal(self) -> None:
        with open(self.filename, 'w') as file:
            file.writelines("{}\n".format(l) for l in self.entries)

    def list_entry(self) -> None:
        print('\n')
        for idx, entry in enumerate(reversed(self.entries), 1):
            print('[{}] {}'.format(idx, entry))

    def add_entry(self, text) -> None:
        if text:
            self.entries.append(text)
