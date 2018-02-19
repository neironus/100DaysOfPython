def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    result = ""

    if number == 0:
        return "0."+("0"*decimals)+suffix

    for x in range(len(powers)-1,-1,-1):
        power = base ** x
        if abs(number) >= power:
            result = number / power

            if decimals == 0:
                result = int(result)
            else:
                result = '{:.{}f}'.format(result, decimals)

            break;

    return str(result)+powers[x] + suffix;


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(-150, base=100, decimals=1, powers=["","d","D"]) == '-1.5d', '-1.5d'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
