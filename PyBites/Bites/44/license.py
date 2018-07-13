import random
import string

chars_allowd = string.ascii_uppercase + string.digits


def gen_key(parts=4, chars_per_part=8):
    result = []

    for _ in range(parts):
        result.append(''.join(random.choice(chars_allowd) for _ in range(chars_per_part)))

    return '-'.join(result)

