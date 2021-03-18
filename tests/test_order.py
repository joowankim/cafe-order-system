from unittest import TestCase

from orders.VO.order import Order


class TestOrder(TestCase):
    def test_order_equals(self):
        customer_info = "Johnn"
        product = "americano"
        amount = 1
        price = 3000

        first = Order(
            customer_info=customer_info,
            product=product,
            amount=amount,
            price=price
        )

        second = Order(
            customer_info=customer_info,
            product=product,
            amount=amount,
            price=price
        )

        third = Order(
            customer_info=customer_info,
            product=product,
            amount=amount,
            price=price
        )

        other = Order(
            customer_info=customer_info,
            product=product,
            amount=amount+12,
            price=price
        )

        self.assertTrue(first == first)

        self.assertTrue(first == second)
        self.assertTrue(second == first)

        self.assertTrue(first == second)
        self.assertTrue(second == third)
        self.assertTrue(first == third)

        self.assertNotEqual(first, other)

