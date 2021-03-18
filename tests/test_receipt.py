from datetime import datetime
from unittest import TestCase

from orders.VO.receipt import Receipt


class TestReceipt(TestCase):
    def test_receipt_equals(self):
        customer_info = "John"
        seller_name = "mime"
        product = "americano"
        price = 3000
        amount = 2
        ordered_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        first = Receipt(
            customer_name=customer_info,
            seller_name=seller_name,
            product=product,
            price=price,
            amount=amount,
            ordered_date=ordered_date)

        second = Receipt(
            customer_name=customer_info,
            seller_name=seller_name,
            product=product,
            price=price,
            amount=amount,
            ordered_date=ordered_date)

        third = Receipt(
            customer_name=customer_info,
            seller_name=seller_name,
            product=product,
            price=price,
            amount=amount,
            ordered_date=ordered_date)

        other = Receipt(
            customer_name=customer_info,
            seller_name=seller_name,
            product=product,
            price=price,
            amount=amount+1,
            ordered_date=ordered_date)

        self.assertTrue(first == first)

        self.assertTrue(first == second)
        self.assertTrue(second == first)

        self.assertTrue(first == second)
        self.assertTrue(second == third)
        self.assertTrue(first == third)

        self.assertNotEqual(first, other)

