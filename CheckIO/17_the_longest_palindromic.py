def longest_palindromic(text):
    palin = []
    
    
    for i in range(len(text)):
        for j in range(i,len(text)+1):
            if text[i:j:] == text[i:j:][::-1]:
                palin.append(text[i:j:])
    
    return sorted(palin, key = lambda x: len(x), reverse = True)[0]

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
