def checkio(expression):
    opening = '([{';
    closing = ')]}';
    currentString = []
    
    for c in expression:
        if c in opening:
            currentString.append(c)
        elif c in closing:
            if len(currentString) == 0 or opening.index(currentString.pop(-1)) != closing.index(c):
                return False

    return currentString == []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False, "Custom 1"