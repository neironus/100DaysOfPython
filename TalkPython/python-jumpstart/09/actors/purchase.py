class Purchase(object):
    """
    Purchase of a house
    """
    def __init__(self, street: str, city: str, zip: str, state: str, beds: int,
                 baths: int, sq__ft: int, type: str, sale_date: str,
                 price: float, latitude: float, longitude: float):
        """
        Init a purchase

        :param str street: A street
        :param str city: A city
        :param str zip: A zip
        :param str state: A US state
        :param int beds: Number of beds
        :param int baths: Number of bathsrooms
        :param int sq__ft: Size of property
        :param str type: Type of property
        :param str sale_date: The date of sale
        :param float price: Price
        :param float latitude: Latitude of property
        :param float longitude: Longitude of property
        """
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft = sq__ft
        self.type = type
        self.sale_date = sale_date
        self.price = price
        self.latitute = latitude
        self.longitude = longitude

    @staticmethod
    def create_from_dict(d) -> object:
        """
        Create a purchase form a dict

        :param dict d: Dictionary containing the data

        :return: A purchase
        :rtype: object
        """
        return Purchase(
            d['street'],
            d['city'],
            d['zip'],
            d['state'],
            int(d['beds']),
            int(d['baths']),
            int(d['sq__ft']),
            d['type'],
            d['sale_date'],
            float(d['price']),
            float(d['latitude']),
            float(d['longitude']),
        )
