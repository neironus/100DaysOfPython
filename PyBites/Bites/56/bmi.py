import argparse


def calc_bmi(weight, length):
    """Provided/done:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Calculate your BMI.',
    )
    parser.add_argument(
        '-w', '--weight',
        dest='weight',
        help='Your weight in kg',
        required=True
    )
    parser.add_argument(
        '-l', '--length',
        dest='length',
        help='Your length in cm',
        required=True
    )

    return parser


def handle_args(args=None):
    """Provided/done:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print('Your BMI is: {}'.format(bmi))


if __name__ == '__main__':
    handle_args()
