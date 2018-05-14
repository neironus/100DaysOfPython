from datetime import date


def print_header():
    print('----------------------------')
    print('     Birthday app')
    print('----------------------------')


def get_user_birthday() -> date:
    print('\n> When were you born?')
    try:
        day = int(input('Day [DD] '))
        month = int(input('Month [MM] '))
        year = int(input('Year [YYYY] '))

        return date(year, month, day)
    except Exception:
        print('> Date not valid')
        return get_user_birthday()


def get_diffences_days(first_date: date, second_date: date) -> int:
    same_year = date(first_date.year, second_date.month, second_date.day)

    return (same_year - first_date).days


def print_birthday_difference(diff_days: int):
    if diff_days > 0:
        print('Your birthday is in {} days'.format(diff_days))
    elif diff_days < 0:
        print('Your birthday was {} days ago'.format(-diff_days))
    else:
        print('Happy birthday')


def main():
    print_header()
    birthday = get_user_birthday()
    diff_days = get_diffences_days(date.today(), birthday)
    print_birthday_difference(diff_days)


if __name__ == '__main__':
    main()
