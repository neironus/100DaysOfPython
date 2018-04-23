import os
import csv
from collections import namedtuple
import re
datas = []

fieldnames = """respd_id do_you_celebrate main_dish main_dish_other
    main_dish_cooked main_dish_cooked_other kind_stuffing
    kind_stuffing_other kind_cranberry kind_cranberry_other
    gravy s_dishes_brussel s_d_carrot s_d_cauliflower s_d_corn
    s_d_cornbread s_d_fruit_salad s_d_beans s_d_macaroni
    s_d_mashed_potatoes s_d_rolls s_d_squash s_d_salad s_d_potato
    s_d_other s_d_other_d pie_apple pie_buttermilk pie_cherry pie_chocolate
    pie_coconut pie_lime pie_peach pie_pecan pim_pumpkin pie_potato
    pie_none pie_other pie_other_d des_apple des_blondies des_brownies
    des_carrot des_cheesecake des_cookies des_fudge des_ice_cream des_peach
    des_none des_other des_other_d pray distance wa_macys cu_kids ht_friends
    friendsgiving black_friday work_retail employer_work_bf describe_where
    age gender total_money_household us_region
    """.split()

Record = namedtuple('Record', ", ".join(fieldnames))


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(
        base_folder, 'data', 'thanksgiving-2015-poll-data.csv'
    )

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin, fieldnames=fieldnames)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            record = Record(**row)
            datas.append(record)


def get_list_regions():
    regions = list(set([x.us_region for x in datas]))
    regions.remove('')

    return regions


def sort_moneys(range):
    r = re.search(r'\$(\d+)', range)  # Extract first number

    if r is not None:
        return int(r.groups()[0])

    return -1


def get_moneys_ranges():
    moneys_ranges = list(set([x.total_money_household for x in datas]))
    moneys_ranges.remove('')
    moneys_ranges.remove('Prefer not to answer')

    return sorted(moneys_ranges, key=sort_moneys)


def records_for_region_and_money(region, money):
    return [
        r for r in datas if r.us_region == region and
        r.total_money_household == money
    ]
