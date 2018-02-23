def checkio(matrix):
    print('######')
    
    #vertical
    vertical = []
    for x in range(len(matrix)):
        vertical.append([])

    for m in matrix:
        for x in range(len(m)):
            vertical[x].append(m[x])
    
    #diagonale
    diagonale = []
    
    #0,0 to len,0
    y = 0
    while y < len(matrix):
        tmp = y
        x = 0
        d = []
        
        while tmp >= 0:
            d.append(matrix[x][tmp])
            tmp -= 1
            x += 1
        else:
            if len(d) >= 4:
                diagonale.append(d)
        
        y += 1
    
    #1,len to len,len
    x = 1
    while x < len(matrix):
        tmp = x
        y = len(matrix)-1
        d = []
        
        while tmp < len(matrix):
            d.append(matrix[tmp][y])
            tmp += 1
            y -= 1
        else:
            if len(d) >= 4:
                diagonale.append(d)
        
        x += 1

    #len,0 to len,len
    y = 0
    while y < len(matrix):
        tmp = y
        x = len(matrix)-1
        d = []
        
        while tmp >= 0:
            d.append(matrix[x][tmp])
            tmp -= 1
            x -= 1
        else:
            if len(d) >= 4:
                diagonale.append(d)
        
        y += 1
    
    #len-1,len to 0,0
    x = len(matrix) - 2
    while x >= 0:
        tmp = x
        y = len(matrix)-1
        d = []
        
        while tmp >= 0:
            d.append(matrix[tmp][y])
            tmp -= 1
            y -= 1
        else:
            if len(d) >= 4:
                diagonale.append(d)
        
        x -= 1
    
    if check(vertical) or check(matrix) or check(diagonale):
        return True
    
    return False

def check(matrix):
    for m in matrix:
        count = 0
        letter = m[0]
        for x in m:
            if x != letter:
                letter = x
                count = 1
            else:
                count += 1
                if count >= 4:
                    return True
                    
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
