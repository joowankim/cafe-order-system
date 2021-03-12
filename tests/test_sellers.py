from unittest import TestCase

from orders.coffee import Coffee
from orders.customers import Customer
from orders.order import Order
from orders.receipt import Receipt
from orders.sellers import Seller


class TestSeller(TestCase):
    def test_create_receipt(self):
        seller = Seller("Jack")
        customer = Customer("Yuni")
        coffee = Coffee("Americano", 3000)

        order = Order(
            customer_info=customer.name,
            product=coffee.name,
            amount=1,
            price=3000
        )

        expected = Receipt(
            customer_name=order.customer_info,
            seller_name=order.seller_info,
            product=order.product,
            price=order.price,
            amount=order.amount,
            ordered_date=order.ordered)

        receipt = seller.create_receipt(order=order)
        self.assertEqual(expected, receipt)
