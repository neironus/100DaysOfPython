import json
import csv


def write_csv(filename, headers, datas):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(headers)
        for data in datas:
            writer.writerow(data)


def create_nodes(res):
    headers = 'id label'.split()
    datas = [[idx, key] for idx, key in enumerate(res)]
    write_csv('nodes.csv', headers, datas)


def create_edges(res):
    headers = 'Source Target Type Kind Id Label timeset Weight'.split()
    datas = []
    for key, items in res.items():
        for item in items:
            datas.append([key, item, 'Undirected', '', '', '', '', ''])

    write_csv('edges.csv', headers, datas)


def main():
    with open('accounts.json', 'r') as file:
        res = json.load(file)
        # create_nodes(res)
        create_edges(res)
    pass


if __name__ == '__main__':
    main()
