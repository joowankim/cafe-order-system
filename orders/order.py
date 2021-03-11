from datetime import datetime


class Order(object):
    def __init__(self, customer_info: str, seller_info: str, product: str, amount: int, price: int):
        self.customer_info = customer_info,
        self.seller_info = seller_info,
        self.ordered = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        self.product = product,
        self.amount = amount,
        self.price = price
