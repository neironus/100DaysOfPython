def popular_words(text, words):
    print('##############')
    # your code here
    return {w.lower():text.lower().replace(',','').replace('.','').split().count(w) for w in words}


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
