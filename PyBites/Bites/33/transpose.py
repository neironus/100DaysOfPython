def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) == dict:
        return [data.keys(), data.values()]
    else:
        # names = [m.name for m in data]
        # days = [m.since_days for m in data]
        # karma = [m.karma_points for m in data]
        # bitecoin = [m.bitecoin_earned for m in data]
        #
        # return names, days, karma, bitecoin
        return list(zip(*data))
