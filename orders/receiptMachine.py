from datetime import datetime

from orders.coffee import Coffee
from orders.order import Order
from orders.receipt import Receipt


class ReceiptMachine:
    def get_receipt(self, order: Order):
        return Receipt(
            customer_name=order.customer_info,
            seller_name=order.seller_info,
            product=order.product,
            price=order.price,
            amount=order.amount,
            ordered_date=order.ordered
        )
