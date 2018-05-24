import sqlite3
from collections import namedtuple

Detail = namedtuple('detail', 'name address phone_number')


def create_table():
    connection = sqlite3.connect('mydb.db')
    c = connection.cursor()
    c.execute("""
      CREATE TABLE Details (name TEXT, address TEXT, phone_number INT)
    """)
    connection.close()


def insert_data():
    # connection = sqlite3.connect('mydb.db')
    # c = connection.cursor()
    #
    # c.execute("""
    #   INSERT INTO Details VALUES ('wtf', 'My awesome street', 332132)
    # """)
    # connection.commit()
    #
    # connection.close()

    with sqlite3.connect('mydb.db') as connection:
        c = connection.cursor()
        c.execute("""
          INSERT INTO Details VALUES('Johny Bravo', '12 Routes du point', 01234)
        """)


def select_data():
    with sqlite3.connect('mydb.db') as connection:
        c = connection.cursor()

        for row in c.execute('SELECT * FROM Details'):
            detail = Detail(*row)
            print('Name: {} Address: {} Phone: {}'.format(
                detail.name, detail.address, detail.phone_number
            ))


def main():
    # create_table()
    # insert_data()
    select_data()


if __name__ == '__main__':
    main()
