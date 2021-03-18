from dataclasses import dataclass
from datetime import datetime


@dataclass(eq=True)
class Order(object):
    def __init__(self, customer_info: str, product: str, amount: int, price: int):
        self.customer_info = customer_info,
        self.ordered = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        self.product = product,
        self.amount = amount,
        self.price = price
