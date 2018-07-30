def get_profile(name: str, age: str, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError

    if len(sports) > 5:
        raise ValueError

    people = {
        'name': name,
        'age': age,
    }

    if sports:
        people['sports'] = sorted(sports)

    if awards:
        people['awards'] = awards

    return people


if __name__ == '__main__':
    t = get_profile()
    print(t)
