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


def clean_list(answers):
    answers.discard('Other (please specify)')
    answers.discard('None')
    answers.discard('I don\t know')
    answers.discard('')

    return answers


def print_answers(txt, answers):
    answers = clean_list(answers)
    print('\n{:#^30}'.format(txt))
    for answer in list(answers):
        print(answer)
    print('{:#^30}'.format(''))


def print_others_meals_choice(region, money):
    print('\n\n')
    print('####################################')
    print('Classic foods choice in your regions')
    print('####################################\n')

    records = research.records_for_region_and_money(region, money)
    main_dishes = set()
    side_dishes = set()
    pies = set()
    desserts = set()

    for r in records:
        main_dishes.update([r.main_dish, r.main_dish_other])

        side_dishes.update([
            r.s_dishes_brussel, r.s_d_carrot, r.s_d_cauliflower, r.s_d_corn,
            r.s_d_cornbread, r.s_d_fruit_salad, r.s_d_beans, r.s_d_macaroni,
            r.s_d_mashed_potatoes, r.s_d_rolls, r.s_d_squash, r.s_d_salad,
            r.s_d_potato, r.s_d_other, r.s_d_other_d
        ])

        pies.update([
            r.pie_apple, r.pie_buttermilk, r.pie_cherry, r.pie_chocolate,
            r.pie_coconut, r.pie_lime, r.pie_peach, r.pie_pecan, r.pim_pumpkin,
            r.pie_potato, r.pie_none, r.pie_other, r.pie_other_d
        ])

        desserts.update([
            r.des_apple, r.des_blondies, r.des_brownies,
            r.des_carrot, r.des_cheesecake, r.des_cookies, r.des_fudge,
            r.des_ice_cream, r.des_peach, r.des_none, r.des_other,
            r.des_other_d
        ])

    print_answers('Main dishes', main_dishes)
    print_answers('Side dishes', side_dishes)
    print_answers('Pies', pies)
    print_answers('Desserts', desserts)


def main():
    research.init()

    # Ask region
    regions = research.get_list_regions()
    region_id = ask_for_region(regions)

    # Ask money
    moneys_ranges = research.get_moneys_ranges()
    money_id = ask_for_household_budget(moneys_ranges)

    print_others_meals_choice(regions[region_id], moneys_ranges[money_id])


if __name__ == '__main__':
    main()
