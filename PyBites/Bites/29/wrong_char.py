def get_index_different_char(chars):
    alpha = []
    nonalpha = []

    for idx, char in enumerate(chars):
        if type(char) is int or char.lower().isalpha():
            alpha.append(idx)
        else:
            nonalpha.append(idx)

    return nonalpha[0] if len(alpha) > len(nonalpha) else alpha[0]


if __name__ == '__main__':
    inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E231
    )
    expected = [2, 4, 1, 5, 8]

    for arg, exp in zip(inputs, expected):
        d = get_index_different_char(arg)
        print(d)
