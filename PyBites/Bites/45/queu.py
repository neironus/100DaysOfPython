from collections import deque

# LOL
# def queue(n=5):
    # return deque(maxlen=n)


class queue:
    def __init__(self, n=5):
        self.n = n
        self.q = deque([])

    def append(self, i):
        if len(self.q) >= self.n:
            self.q.popleft()

        self.q.append(i)

    def __iter__(self):
        for elm in self.q:
            yield(elm)


if __name__ == '__main__':
    q = queue()
    for i in range(10):
        q.append(i)
        print((i, list(q)))

    """Queue size does not go beyond n (int), this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """
