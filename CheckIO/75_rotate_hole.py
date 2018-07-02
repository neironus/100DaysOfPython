def cannonball_fill(state, pipe_numbers):
    results = [True for pipe in pipe_numbers if state[pipe] == 1]

    return len(results) == len(pipe_numbers)


def rotate(state, pipe_numbers):
    results = []
    if cannonball_fill(state, pipe_numbers):
        results.append(0)

    for x in range(1, len(state)):
        last = state.pop()
        state = [last] + state

        if cannonball_fill(state, pipe_numbers):
            results.append(x)

    return results


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
