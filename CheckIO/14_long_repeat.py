def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    i = 0
    result = 0

    while i < len(line):
        j = 1
        tmp = 1

        while i+j < len(line):
            if line[i] == line[i+j]:
                tmp += 1
                j += 1
            else:
                break

        if tmp > result:
            result = tmp

        i += 1

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
