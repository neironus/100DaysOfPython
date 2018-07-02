import os
import csv
import statistics
from collections import defaultdict

from typing import List

from actors.purchase import Purchase


def print_headers():
    print('-----------------------------------------')
    print('      REAL ESTATE DATA MINING APP')
    print('-----------------------------------------')
    print()


def get_data_fullpath(filename: str) -> str:
    """
    Get the full path of file located in folder data

    :param str filename: Name of the file

    :return: Full path
    :rtype: str
    """
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', filename)


def get_datas() -> List[Purchase]:
    """
    Get all the datas from the file

    :return: Datas
    :rtype: List[Purchase]
    """
    full_path = get_data_fullpath('SacramentoRealEstateTransactions2008.csv')

    with open(full_path) as file:
        reader = csv.DictReader(file)
        return [Purchase.create_from_dict(row) for row in reader]


def order_by_price(purchases: List[Purchase]) -> List[Purchase]:
    """
    Sorted the purchases by price. Cheapest first

    :param List[Purchase] purchases: List of purchases

    :return: Purchases ordered by cheapest price
    :rtype: List[Purchase]
    """
    return sorted(purchases, key=lambda x: x.price)


def most_expensive(purchases: List[Purchase]) -> None:
    """
    Print the most expensive purchase

    :param List[Purchase] purchases: List of purchases

    :return: None
    :rtype: None
    """
    purchases = order_by_price(purchases)

    house = purchases[-1]

    print('Most expensive house: {}-bed {}-bath house for ${:.0f} in {}'.format(
        house.beds,
        house.baths,
        house.price,
        house.city
    ))


def least_expensive(purchases: List[Purchase]) -> None:
    """
    Print the cheapest purchase

    :param List[Purchase] purchases: List of purchase

    :return: None
    :rtype: None
    """

    purchases = order_by_price(purchases)
    house = purchases[0]

    print('Cheapest house: {}-bed {}-bath house for ${:.0f} in {}'.format(
        house.beds,
        house.baths,
        house.price,
        house.city
    ))


def calc_average_purchases(purchases: List[Purchase]) -> dict:
    """
    Calculate the average of price, rooms, bathrooms for a list of purchases 
    
    :param List[Purchase] purchases: List of purchases
    
    :return: dict containing the avg of price, rooms, bathrooms
    :rtype: dict
    """
    avg = defaultdict(list)

    for purchase in purchases:
        avg['price'].append(purchase.price)
        avg['beds'].append(purchase.beds)
        avg['baths'].append(purchase.baths)

    return {
        'price': statistics.mean(avg['price']),
        'beds': statistics.mean(avg['beds']),
        'baths': statistics.mean(avg['baths'])
    }


def average_purchase(purchases: List[Purchase]) -> None:
    """
    Print the avg price/beds/bath of all purchases

    :param List[Purchase] purchases: List of all purchases

    :return: None
    :rtype: None
    """
    avg = calc_average_purchases(purchases)

    print('Average purchase: ${:.0f}, {:.1f} bed, {:.1f} bath.'.format(
        avg.get('price'),
        avg.get('beds'),
        avg.get('baths')
    ))


def average_2_bedrooms(purchases: List[Purchase]) -> None:
    """
    Print the avg price/beds/baths for purchase with only 2 beds

    :param List[Purchase] purchases: List of purchases

    :return: None
    :rtype: None
    """
    avg = calc_average_purchases(
        (purchase for purchase in purchases if purchase.beds == 2)
    )

    print('Average 2-bedroom purchase: ${:.0f}, {:.1f} bed, {:.1f} bath.'
          .format(avg.get('price'), avg.get('beds'), avg.get('baths'))
    )


def main():
    print_headers()
    purchases = get_datas()

    most_expensive(purchases)
    print()
    least_expensive(purchases)
    print()
    average_purchase(purchases)
    print()
    average_2_bedrooms(purchases)


if __name__ == '__main__':
    main()
