import csv
from logging import exception
from multiprocessing.sharedctypes import Value


class Item:
    pay_rate = 0.8  # The pay rate after 20% of discount
    all = []  # array to store all the instances of the class

    # java==constructor method
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received attributes
        assert price >= 0, f"Price {price} can't be < 0!"
        assert quantity >= 0, f"quantity {quantity} can't be < 0!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("name too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, inc_value):
        self.__price = self.__price * (1 + inc_value)

    @classmethod
    def instantiate_from_csv(cls):
        with open('sell_store\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # count out the floats that are point zero: e.g.: 5.0 10.0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True

    # java==toString method; the output is as the source code; python standard
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
