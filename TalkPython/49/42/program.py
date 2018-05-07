import research


def print_options_choice(choices, fnc, *args):
    for idx, choice in enumerate(choices):
        print('{} for {}'.format(idx, choice))

    inp = input('\n')
    # If input not valid then call the function again
    if not inp.isdigit() or not 0 <= int(inp) < len(choices):
        print('Invalid value\n\n')
        return fnc(*args)
    else:
        return int(inp)


def ask_for_region(regions):
    print('Your region ? Enter :')
    return print_options_choice(regions, ask_for_region, regions)


def ask_for_household_budget(moneys_ranges):
    print('Your household budget ? Enter :')
    return print_options_choice(
        moneys_ranges, ask_for_household_budget, moneys_ranges
    )


def main():
    research.init()

    # Ask region
    regions = research.get_list_regions()
    region_id = ask_for_region(regions)

    # Ask money
    moneys_ranges = research.get_moneys_ranges()
    money_id = ask_for_household_budget(moneys_ranges)

    research.print_others_meals_choice(regions[region_id],
                                       moneys_ranges[money_id])


if __name__ == '__main__':
    main()
