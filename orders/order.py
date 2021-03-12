from datetime import datetime


class Order(object):
    def __init__(self, customer_info: str, product: str, amount: int, price: int):
        self.customer_info = customer_info,
        self.ordered = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        self.product = product,
        self.amount = amount,
        self.price = price

    def __eq__(self, other):
        return (self.customer_info == other.customer_info and
                self.ordered == other.ordered and
                self.product == other.product and
                self.amount == other.amount and
                self.price == other.price)
