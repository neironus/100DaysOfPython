from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expire):
        self.name = name
        self.expire = expire
    
    @property
    def expired(self):
        return NOW > self.expire
