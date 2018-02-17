def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    return sorted(data, key = lambda x: data.count(x), reverse = True)[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    assert most_frequent(['a', 'a', 'z']) == 'a'
    print('Done')
