from typing import List


def load_dictionary():
    """
    Load the dictionary of words
    """
    with open('dico.txt') as fl:
        for line in fl:
            yield line.strip()


def word_match_sequence(word: str, seq: List[int]):
    """
    Check if the word is compatible with the sequence
    :param word: The word
    :param seq: The sequence to find
    :return: True if seq match, false otherwise
    """
    for idx, v in enumerate(seq):
        if word.count(word[idx]) != seq.count(v):
            return False

    return True


def main():
    """
    Main function
    """

    dictionary = load_dictionary()
    seq = input('Sequence to find separate by , (comma): ').split(',')

    # Debug options, "concernant" = OK
    # dictionary = ['concernant', 'anagrammes', 'bob']
    # seq = [0, 1, 2, 0, 3, 4, 2, 5, 2, 6]

    for word in dictionary:
        if len(word) != len(seq):
            continue

        if word_match_sequence(word, seq):
            print(word)


if __name__ == '__main__':
    main()
