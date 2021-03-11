from orders.coffee import Coffee
from orders.order import Order
from orders.receiptMachine import ReceiptMachine


class Seller:
    def __init__(self, name: str):
        self.name = name
        self.machine = ReceiptMachine()

    def create_receipt(self, order: Order):
        return self.machine.get_receipt(order=order)
