import math

def checkio(a, b, c):

    try:
        aa = round(math.degrees(math.acos((b*b + c*c - a*a)/(2*b*c))))
        ba = round(math.degrees(math.acos((c*c + a*a - b*b)/(2*c*a))))
        ca = round(math.degrees(math.acos((a*a + b*b - c*c)/(2*a*b))))

        if aa != 180 and ba != 180 and ca != 180:
            return sorted([aa,ba,ca])
        else:
            return [0,0,0]
    except:
        return [0,0,0]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
