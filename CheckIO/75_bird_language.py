VOWELS = "aeiouy"


def get_word(letters):
    correct = []
    skip = 0

    for idx, l in enumerate(letters):
        if skip > 0:
            skip -= 1
            continue

        if l not in VOWELS:
            if letters[idx + 1] in VOWELS:
                skip = 1
                correct.append(l)
        else:
            if letters[idx + 1] == l and letters[idx + 2] == l:
                skip = 2
                correct.append(l)

    return ''.join(correct)


def translate(phrase):
    words = []
    for letters in phrase.split():
        words.append(get_word(letters))

    return ' '.join(words)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
