from orders.order import Order
from orders.receipt import Receipt
from orders.receiptMachine import ReceiptMachine


class Seller:
    def __init__(self, name: str):
        self.name = name
        self.machine = ReceiptMachine()

    def create_receipt(self, order: Order) -> Receipt:
        return self.machine.get_receipt(seller_name=self.name, order=order)
