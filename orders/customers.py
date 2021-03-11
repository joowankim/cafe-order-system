from datetime import datetime

from orders.coffee import Coffee
from orders.receipt import Receipt
from orders.sellers import Seller


class Customer:
    def __init__(self, name: str):
        self.name = name

    def order_coffee(self, coffee: Coffee):
        ordered_date = datetime(2021, 3, 9, 10, 23, 43)
        seller = Seller("Ami")
        return Receipt(
            seller_name=seller.name,
            product=coffee.name,
            price=3000,
            amount=1,
            ordered_date=ordered_date.strftime("%m/%d/%Y, %H:%M:%S"))
