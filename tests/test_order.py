import unittest
from datetime import datetime

from orders.receipts import Receipt
from orders.sellers import Seller
from orders.customers import Customer
from orders.coffee import Coffee


class TestOrder(unittest.TestCase):
    def test_order_coffee(self):
        coffee = Coffee("Americano")
        seller = Seller("Jin")
        customer = Customer("John", seller)
        ordered_date = datetime(2021, 3, 9, 10, 23, 43)

        receipt = customer.order_coffee(coffee)

        expected = Receipt(
            customer_name=customer.name,
            seller_name=seller.name,
            product=coffee.name,
            price=3000,
            amount=1,
            ordered_date=ordered_date.strftime("%m/%d/%Y, %H:%M:%S"))

        # casher = Casher("Amy")
        self.assertEqual(expected, receipt)


if __name__ == '__main__':
    unittest.main()
