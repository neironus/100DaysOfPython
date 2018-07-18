from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number: int, title: str):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self, value):
        return ''

    @property
    def pretty_title(self):
        return ''



class BlogChallenge(Challenge):
    def __init__(self, number: int, title: str, merged_prs: list):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, value):
        return value in self.merged_prs

    @property
    def pretty_title(self):
        return 'PCC{} - {}'.format(self.number, self.title)


class BiteChallenge(Challenge):
    def __init__(self, number: int, title: str, result: str):
        super().__init__(number, title)
        self.result = result
        self._pretty_title = 'Bite {}. {}'.format(number, title)

    def verify(self, value):
        return value == self.result

    @property
    def pretty_title(self):
        return 'Bite {}. {}'.format(self.number, self.title)


if __name__ == '__main__':
    c = Challenge()

    bc = BlogChallenge()
