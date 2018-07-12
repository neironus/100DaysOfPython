names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    for idx, (name, country) in enumerate(zip(names, countries), 1):
        print('{}. {} {}'.format(idx, name, country))
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    pass


if __name__ == '__main__':
    enumerate_names_countries()
