from datetime import datetime

from orders.coffee import Coffee
from orders.receipts import Receipt
from orders.sellers import Seller


class Customer:
    def __init__(self, name: str, seller: Seller):
        self.name = name
        self.seller = seller

    def order_coffee(self, coffee: Coffee):
        ordered_date = datetime(2021, 3, 9, 10, 23, 43)
        return Receipt(
            customer_name=self.name,
            seller_name=self.seller.name,
            product=coffee.name,
            price=3000,
            amount=1,
            ordered_date=ordered_date.strftime("%m/%d/%Y, %H:%M:%S"))
