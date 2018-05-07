import os
import csv
from collections import namedtuple
import re
datas = []

saved_result = {}

mains_dishes_fields = "main_dish main_dish_other"
side_dishes_fields = """s_dishes_brussel s_d_carrot s_d_cauliflower s_d_corn
    s_d_cornbread s_d_fruit_salad s_d_beans s_d_macaroni
    s_d_mashed_potatoes s_d_rolls s_d_squash s_d_salad s_d_potato
    s_d_other s_d_other_d"""

pie_fields = """pie_apple pie_buttermilk pie_cherry pie_chocolate
    pie_coconut pie_lime pie_peach pie_pecan pim_pumpkin pie_potato
    pie_none pie_other pie_other_d"""

desserts_fields = """des_apple des_blondies des_brownies
    des_carrot des_cheesecake des_cookies des_fudge des_ice_cream des_peach
    des_none des_other des_other_d"""

fieldnames = """respd_id do_you_celebrate {}
    main_dish_cooked main_dish_cooked_other kind_stuffing
    kind_stuffing_other kind_cranberry kind_cranberry_other
    gravy {} {} {} pray distance wa_macys cu_kids ht_friends
    friendsgiving black_friday work_retail employer_work_bf describe_where
    age gender total_money_household us_region
    """.format(mains_dishes_fields, side_dishes_fields,
               pie_fields, desserts_fields).split()

Record = namedtuple('Record', ", ".join(fieldnames))


def init():
    if datas:
        return

    base_folder = os.path.dirname(__file__)
    filename = os.path.join(
        base_folder, 'data', 'thanksgiving-2015-poll-data.csv'
    )

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin, fieldnames=fieldnames)
        for idx, row in enumerate(reader):
            if idx == 0:  # Ignore the first row because header
                continue

            record = Record(**row)
            datas.append(record)


def get_list_regions():
    regions = set([x.us_region for x in datas])
    return list(cleanning(regions))


def sort_moneys(range):
    r = re.search(r'\$(\d+)', range)  # Extract first number

    if r is not None:
        return int(r.groups()[0])

    return -1


def get_moneys_ranges():
    moneys_ranges = set([x.total_money_household for x in datas])
    moneys_ranges = list(cleanning(moneys_ranges))

    return sorted(moneys_ranges, key=sort_moneys)


def records_for_region_and_money(region, money):
    return [
        r for r in datas if r.us_region == region and
        r.total_money_household == money
    ]


# Remove undesired answers
def cleanning(answers):
    answers.discard('Other (please specify)')
    answers.discard('None')
    answers.discard('I don\t know')
    answers.discard('')
    answers.discard('Prefer not to answer')

    return answers


def print_answers(txt, answers):
    if answers:
        answers = cleanning(answers)
        print('\n{:#^30}'.format(txt))
        for answer in list(answers):
            print(answer)
        print('{:#^30}'.format(''))


# Get value for each fields
def get_value_for_fields(record, fields):
    return [getattr(record, field) for field in fields.split()]


def add_to_saved_result(region, money, meal, datas):
    if not saved_result.get(region):
        saved_result[region] = {}

    if not saved_result.get(region).get(money):
        saved_result[region][money] = {}

    if not saved_result.get(region).get(money).get(meal):
        saved_result[region][money][meal] = datas


def print_others_meals_choice(region, money):
    print('\n\n')
    print('####################################')
    print('Classic foods choices in your region')
    print('####################################\n')

    try:
        cached = saved_result.get(region).get(money)
        main_dishes = cached.get('main_dishes')
        side_dishes = cached.get('side_dishes')
        pies = cached.get('pies')
        desserts = cached.get('desserts')
    except Exception:
        records = records_for_region_and_money(region, money)

        main_dishes = set()
        side_dishes = set()
        pies = set()
        desserts = set()

        for r in records:
            main_dishes.update(get_value_for_fields(r, mains_dishes_fields))
            side_dishes.update(get_value_for_fields(r, side_dishes_fields))
            side_dishes.update(get_value_for_fields(r, pie_fields))
            desserts.update(get_value_for_fields(r, desserts_fields))

        add_to_saved_result(region, money, 'main_dishes', main_dishes)
        add_to_saved_result(region, money, 'side_dishes', side_dishes)
        add_to_saved_result(region, money, 'pies', pies)
        add_to_saved_result(region, money, 'desserts', desserts)

    print_answers('Main dishes', main_dishes)
    print_answers('Side dishes', side_dishes)
    print_answers('Pies', pies)
    print_answers('Desserts', desserts)

