from gooey import GooeyParser, Gooey


@Gooey(program_name='GUI Test', program_description='My awesome descriptions')
def main():
    args = get_params()

    print(args.text1, args.date)


def get_params():
    parser = GooeyParser()
    parser.add_argument('text1', metavar='Text 1', help='Text 1 help')
    parser.add_argument('date',  metavar='Date', widget='DateChooser')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
