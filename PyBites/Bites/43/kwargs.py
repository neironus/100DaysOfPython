# https://stackoverflow.com/questions/14301967/python-bare-asterisk-in-function-argument
def get_profile(*, name='julian', profession='programmer'):
    return '{} is a {}'.format(name, profession)
