def count(data, pos, total):
    if pos < len(data):
        total += data[pos]
        return count(data, pos+1, total)
    else:
        return total

def checkio(data):
    return count(data, 0, 0)