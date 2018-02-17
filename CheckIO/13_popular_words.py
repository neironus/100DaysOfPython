def popular_words(text, words):
    print('##############')
    # your code here
    result = {}

    for w in words:
        result[w.lower()] = 0


    text = text.split()

    for t in text:
        tl = t.lower().strip(',.')
        if tl in words:
            if tl in result:
                result[tl] += 1

    return result



if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'two', 'three']) == {
        'i': 4,
        'two': 1,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
